from fastmcp import FastMCP
import requests
import os
import logging
import json
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("gitlab-mcp")

load_dotenv()

mcp = FastMCP("gitlab-mcp")

GITLAB_BASE_URL = "https://gitlab.com/api/v4"

def get_headers():
    token = os.environ.get("GITLAB_PERSONAL_ACCESS_TOKEN")
    if not token:
        logger.error("GITLAB_PERSONAL_ACCESS_TOKEN not found in environment variables")
        raise ValueError("GITLAB_PERSONAL_ACCESS_TOKEN not set")
    
    # Log masked token for debugging purposes
    safe_token = f"{token[:4]}...{token[-4:]}" if len(token) > 8 else "****"
    logger.debug(f"Computed Headers: {{'PRIVATE-TOKEN': '{safe_token}'}}")
    
    return {"PRIVATE-TOKEN": token}

# --- Implementation Logic ---

def mr_search_logic(projectId: str, state: str, search_param: str = None, search: str = None, target_branch: str = None) -> str:
    """Implementation of mr_search."""
    logger.debug(f"Calling mr_search with projectId={projectId}, state={state}, search={search}, target_branch={target_branch}")
    
    url = f"{GITLAB_BASE_URL}/projects/{projectId}/merge_requests"
    params = {"state": state}
    
    if search_param:
        params["in"] = search_param
    if search:
        params["search"] = search
    if target_branch:
        params["target_branch"] = target_branch
        
    try:
        response = requests.get(url, headers=get_headers(), params=params)
        logger.debug(f"GitLab API Response Status: {response.status_code}")
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.exception("Error in mr_search")
        return str(e)

def mr_info_logic(projectId: str, mergeRequestId: str) -> str:
    """Implementation of mr_info."""
    logger.debug(f"Calling mr_info with projectId={projectId}, mergeRequestId={mergeRequestId}")
    url = f"{GITLAB_BASE_URL}/projects/{projectId}/merge_requests/{mergeRequestId}"
    
    try:
        response = requests.get(url, headers=get_headers())
        logger.debug(f"GitLab API Response Status: {response.status_code}")
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.exception("Error in mr_info")
        return str(e)

def mr_diff_logic(projectId: str, mergeRequestId: str, page: int = 1, per_page: int = 20) -> str:
    """Implementation of mr_diff."""
    logger.debug(f"Calling mr_diff with projectId={projectId}, mergeRequestId={mergeRequestId}, page={page}, per_page={per_page}")
    url = f"{GITLAB_BASE_URL}/projects/{projectId}/merge_requests/{mergeRequestId}/diffs"
    params = {"page": page, "per_page": per_page}
    
    try:
        response = requests.get(url, headers=get_headers(), params=params)
        logger.debug(f"GitLab API Response Status: {response.status_code}")
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.exception("Error in mr_diff")
        return str(e)

@mcp.tool(name="mr_diff_paged")
def mr_diff_paged(projectId: str, mergeRequestId: str, page: int = 1, per_page: int = 20) -> str:
    """
    Read contents (diffs) of a merge request with pagination.
    
    Args:
        projectId: The ID of the project.
        mergeRequestId: The IID of the merge request.
        page: Page number (default 1).
        per_page: Number of changes to return (defaults to 20).
    """
    return mr_diff_logic(projectId, mergeRequestId, page, per_page)

@mcp.tool(name="mr_diff")
def mr_diff(projectId: str, mergeRequestId: str, per_page: int = 20) -> str:
    """
    Read contents (diffs) of a merge request.
    
    Args:
        projectId: The ID of the project.
        mergeRequestId: The IID of the merge request.
        per_page: Number of changes to return (defaults to 20).
    """
    return mr_diff_logic(projectId, mergeRequestId, page=1, per_page=per_page)

def mr_review_comment_logic(projectId: str, mergeRequestId: str, base_sha: str, head_sha: str, start_sha: str, new_path: str, old_path: str, comment_line_number: int, content: str) -> str:
    """Implementation of mr_review_comment."""
    logger.debug(f"Calling mr_review_comment on {new_path}:{comment_line_number}")
    url = f"{GITLAB_BASE_URL}/projects/{projectId}/merge_requests/{mergeRequestId}/discussions"
    
    data = {
        "position[position_type]": "text",
        "position[base_sha]": base_sha,
        "position[head_sha]": head_sha,
        "position[start_sha]": start_sha,
        "position[new_path]": new_path,
        "position[old_path]": old_path,
        "position[new_line]": comment_line_number,
        "body": content
    }
    
    try:
        response = requests.post(url, headers=get_headers(), data=data)
        logger.debug(f"GitLab API Response Status: {response.status_code}")
        if not response.ok:
            logger.error(f"GitLab API Error Response: {response.text}")
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.exception("Error in mr_review_comment")
        return str(e)

def project_search_logic(project_name: str) -> str:
    """Implementation of project_search."""
    logger.debug(f"Calling project_search with project_name={project_name}")
    url = f"{GITLAB_BASE_URL}/projects"
    params = {"search": project_name}
    
    try:
        response = requests.get(url, headers=get_headers(), params=params)
        logger.debug(f"GitLab API Response Status: {response.status_code}")
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.exception("Error in project_search")
        return str(e)

# --- MCP Tool Registrations ---

@mcp.tool(name="mr_search")
def mr_search(projectId: str, state: str, search_param: str = None, search: str = None, target_branch: str = None) -> str:
    """
    Search for merge request ID.
    
    Args:
        projectId: The ID of the project.
        state: The state of the MR (opened, closed, locked, merged).
        search_param: Optional. 'title', 'description', or 'title,description'. Mandatory if regex is used in search.
        search: Optional. Search query (e.g., 'ALPS-5573' or regex).
        target_branch: Optional. Target branch (e.g., 'master', 'develop').
    """
    return mr_search_logic(projectId, state, search_param, search, target_branch)

@mcp.tool(name="mr_info")
def mr_info(projectId: str, mergeRequestId: str) -> str:
    """
    Get detailed information of a merge request.
    
    Args:
        projectId: The ID of the project.
        mergeRequestId: The IID of the merge request.
    """
    return mr_info_logic(projectId, mergeRequestId)



@mcp.tool(name="mr_review_comment")
def mr_review_comment(projectId: str, mergeRequestId: str, base_sha: str, head_sha: str, start_sha: str, new_path: str, old_path: str, comment_line_number: int, content: str) -> str:
    """
    Write a review comment on a merge request.
    
    Args:
        projectId: The ID of the project.
        mergeRequestId: The IID of the merge request.
        base_sha: Base SHA from MR info.
        head_sha: Head SHA from MR info.
        start_sha: Start SHA from MR info.
        new_path: File new path.
        old_path: File old path.
        comment_line_number: Line number for the comment.
        content: The text of the comment.
    """
    return mr_review_comment_logic(projectId, mergeRequestId, base_sha, head_sha, start_sha, new_path, old_path, comment_line_number, content)

@mcp.tool(name="project_search")
def project_search(project_name: str) -> str:
    """
    Search for project ID using project name.
    
    Args:
        project_name: The name of the project to search for.
    """
    return project_search_logic(project_name)

def mr_diff_parser_logic(diff_content: str) -> str:
    """Implementation of mr_diff_parser."""
    logger.debug("Calling mr_diff_parser")
    
    parsed_lines = []
    lines = diff_content.split('\n')
    
    old_line_counter = 0
    new_line_counter = 0
    
    import re
    
    # Regex to parse the chunk header: @@ -old_start,old_count +new_start,new_count @@
    # Note: count is optional and defaults to 1 if not present
    header_regex = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
    
    for line in lines:
        # Check for chunk header
        match = header_regex.match(line)
        if match:
            old_start = int(match.group(1))
            new_start = int(match.group(3))
            
            old_line_counter = old_start
            new_line_counter = new_start
            continue
            
        # Skip if counters are not set (e.g. metadata lines before first chunk)
        if old_line_counter == 0 and new_line_counter == 0:
            continue
            
        if line.startswith(' '):
            # Context line (NA)
            # Both old and new files have this line
            parsed_lines.append({
                "lineNumber": new_line_counter,
                "content": line[1:], # Remove prefix space
                "action": "NA"
            })
            old_line_counter += 1
            new_line_counter += 1
            
        elif line.startswith('+'):
            # Added line
            # Only new file has this line
            parsed_lines.append({
                "lineNumber": new_line_counter,
                "content": line[1:], # Remove prefix +
                "action": "ADDED"
            })
            new_line_counter += 1
            
        elif line.startswith('-'):
            # Removed line
            # Only old file has this line
            parsed_lines.append({
                "lineNumber": old_line_counter,
                "content": line[1:], # Remove prefix -
                "action": "REMOVED"
            })
            old_line_counter += 1
            
        # Ignore other lines (like \ No newline at end of file)
        
    return json.dumps(parsed_lines)

@mcp.tool(name="mr_diff_parser")
def mr_diff_parser(diff_content: str) -> str:
    """
    Parse git diff content to actionable objects.
    
    Args:
        diff_content: The git diff string to parse.
    """
    return mr_diff_parser_logic(diff_content)

if __name__ == "__main__":
    mcp.run()
