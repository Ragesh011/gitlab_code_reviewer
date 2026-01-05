# GitLab Automated Code Reviewer using MCP

This project provides a **GitLab Model Context Protocol (MCP)** server that enables AI Agents (like AntiGravity, Windsurf, or Cursor) to interact with GitLab for automated code reviews. It allows agents to search Merge Requests, fetch diffs, parse changes, and post review comments based on defined coding guidelines.

## 🚀 Setup & Installation

### 1. Clone the Repository
Clone this project to your local machine:
```bash
git clone https://github.com/Ragesh011/gitlab_code_reviewer.git
cd gitlab-code-reviewer
```

### 2. Install Dependencies
Ensure you have Python 3.10+ installed. Install the required packages directly:
```bash
pip install fastmcp requests python-dotenv uvicorn
```

---

## 🔑 Authentication

You must provide a GitLab Personal Access Token for the MCP server to authenticate with the GitLab API.

### Create a GitLab Token
1.  Log in to GitLab.
2.  Click on the **User Icon** (top right corner).
3.  Click **Edit profile**, then select **Access Tokens** from the sidebar.
4.  Click **Add new token**.
4.  **Name**: `MCP-Code-Reviewer` (or similar).
5.  **Scopes**: Select `api` (required for reading MRs and posting comments).
6.  Click **Create personal access token**.
7.  **Copy the token immediately**. You won't see it again.

---

## ⚙️ MCP Server Configuration

Configure your AI Agent/IDE to use this MCP server. The server runs the python script `gitlab_mcp_server.py`.

### Environment Variables
For security, do not hardcode the token in the python script. Instead, pass it via the `env` block in your JSON configuration. Alternatively, you can use a `.env` file in the project root, but the JSON method is preferred for Agent integration.

### For AntiGravity
1.  **Open the Chat Window**.
2.  Click the **...** icon (top right of the window).
3.  Select **MCP Servers**.
4.  Click **Manage MCP Servers**.
5.  Click **View Raw Config**.
6.  Add the following entry to the `mcpServers` object in the opened JSON file:

```json
{
  "mcpServers": {
    "gitlab-mcp": {
      "command": "python3",
      "args": [
        "/absolute/path/to/gitlab-code-reviewer/gitlab_mcp_server.py"
      ],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "your_token_starts_with_glpat-..."
      }
    }
  }
}
```
*Replace `/absolute/path/to/...` with the actual path where you cloned this repo.*

### For Windsurf
1.  **Open the Chat Window**.
2.  Click on the **Plugin Button** (immediately to the left of `...` on the top right corner).
3.  Click on the **Configure Icon** (dual parallel lines) above "MCP Marketplace".
4.  This will open `mcp_config.json`. Add the server configuration:

```json
"gitlab-mcp": {
  "command": "python",
  "args": [
    "/absolute/path/to/gitlab-code-reviewer/gitlab_mcp_server.py"
  ],
  "env": {
    "GITLAB_PERSONAL_ACCESS_TOKEN": "your_token_starts_with_glpat-..."
  }
}
```

**Restart your IDE/Agent** after saving the configuration to load the new tools.

---

## 📝 Coding Guidelines

The reviewer uses coding guidelines to analyze diffs.

### Spring Boot (Default)
The project comes with [`SPRING_BOOT_CODING_GUIDELINES.md`](SPRING_BOOT_CODING_GUIDELINES.md) which contains rules for:
*   Audit fields in Entities.
*   Null safety checks.
*   Magic strings.
*   Service layer logging.

### Using Other Frameworks (Node.js, Python, React, etc.)
If you are reviewing a project that is **not** Spring Boot:
1.  Create a new markdown file, e.g., `REACT_CODING_GUIDELINES.md`.
2.  Define your specific rules (e.g., "Use functional components", "No inline styles").
3.  **Instruct the Agent**: When starting a review, explicitly tell the agent via GITLAB_AUTOMATED_REVIEW_PROCESS.md file:
    > "Read formatting rules from REACT_CODING_GUIDELINES.md instead of the default."

---

## 🛠️ Usage

Once configured, you can ask your Agent to perform tasks like:
*   "Add review comments in gitlab MR having title 'ALPS-5468' for target branch 'master' in project 'triti_eeg'."

The Agent will use tools like `mr_diff_paged`, `mr_diff_parser`, and `mr_review_comment` to execute your request securely.
