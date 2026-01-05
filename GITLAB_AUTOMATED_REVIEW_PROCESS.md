# GitLab Automated Code Review Process

This document describes the implemented Model Context Protocol (MCP) server for GitLab interactions, designed to facilitate automated code reviews with pre-defined review guidelines.

## MCP Server Implementation

### [gitlab_mcp_server.py](file:///Users/ragesh.natarajan/Desktop/antiygravity-projects/gitlab-code-reviewer/gitlab_mcp_server.py)
 - **Framework**: `fastmcp`
 - **Authentication**: Uses `GITLAB_PERSONAL_ACCESS_TOKEN` env variable.
 - **Logging**: Configured to output DEBUG level logs.

### Available Tools

#### `mr_search`
- **Input**: `projectId`, `state`, `search_param`, `search`, `target_branch`
- **Logic**: Search for Merge Requests.
- **Output**: JSON List of MRs.

#### `mr_info`
- **Input**: `projectId`, `mergeRequestId`
- **Logic**: Get detailed metadata for a specific MR (including SHAs and `changes_count`).
- **Output**: JSON object.

#### `mr_diff`
- **Input**: `projectId`, `mergeRequestId`, `per_page` (optional, default 20)
- **Logic**: Fetch diffs for an MR.
- **Output**: JSON List of changes (diffs).

#### `mr_diff_paged`
- **Input**: `projectId`, `mergeRequestId`, `page` (optional, default 1), `per_page` (optional, default 20)
- **Logic**: Fetch diffs page-by-page to handle large reviews.
- **Output**: JSON List of changes.

#### `mr_diff_parser`
- **Input**: `diff_content` (string)
- **Logic**: Parse a single file's git diff string into a structured list.
- **Output**: JSON List of objects `{lineNumber, content, action}`.
    - `action`: `ADDED`, `REMOVED`, or `NA` (Context).

#### `mr_review_comment`
- **Input**: `projectId`, `mergeRequestId`, `base_sha`, `head_sha`, `start_sha`, `new_path`, `old_path`, `comment_line_number`, `content`
- **Logic**: Post a discussion/comment on a specific line of the MR.
- **Rules**: `comment_line_number` must match the NEW file line number for added lines.

#### `project_search`
- **Input**: `project_name`
- **Logic**: Search for a project by name.
- **Output**: JSON List of projects.

## Code Review Workflow

To ensure accurate line tracking and systematic review, Agents **MUST** follow this workflow:

1.  **Read Guidelines**: Always read `SPRING_BOOT_CODING_GUIDELINES.md` to load the latest rules into context.
2.  **Get Info**: Call `mr_info` to get `changes_count`. Use this to calculate the number of pages needed for `mr_diff_paged` (Total Changes / per_page).
3.  **Fetch Strategy**: Use `changes_count` to plan pagination.
    *   Set `per_page` to a safe limit (e.g., 5).
    *   Calculate required pages: `ceil(changes_count / per_page)`.
    *   **Loop**: Call `mr_diff_paged` for each page `1` to `N` to retrieve all file changes.
4.  **Parse**: Pass the `diff` string of each file to `mr_diff_parser`.
5.  **Analyze**: Iterate through the JSON output from the parser.
    *   Only analyze items where `action == "ADDED"`.
    *   Use `lineNumber` from the parser for reporting.
6.  **Comment**: Post violations using `mr_review_comment`.

**Constraint**: Do NOT create temporary local files (e.g., scripts, json dumps) to perform reviews. Rely exclusively on the MCP tool outputs and in-context reasoning.