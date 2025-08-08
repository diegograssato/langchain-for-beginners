from mcp.server.fastmcp import FastMCP
import requests
import logging
import urllib3
import os
from dotenv import load_dotenv

# import dotenv
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL", "").strip()
JIRA_TOKEN = os.getenv("JIRA_TOKEN", "").strip()

# Disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

mcp = FastMCP("jira")

headers: dict[str, str] = {"Content-Type": "application/json"}
headers["Authorization"] = f"Bearer {JIRA_TOKEN}"

@mcp.tool()
async def get_issue(issue_id: str) -> dict:
    """Consulta a API do Jira e retorna dados de uma issue em especifico."""
    issue_id = issue_id.lower().strip()
    url = f"{JIRA_URL}/rest/api/2/issue/{issue_id}"
    logger.info(
                    "Buscando informações sobre a task %s.",
                    issue_id,
                )
    try:

        response = requests.get(url, headers=headers, timeout=20, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao buscar Jira '{issue_id}': {str(e)}"}

@mcp.tool()
async def get_issue_with_subtasks(issue_id: str) -> dict:
    """Consulta a  API do Jira e retorna dados de uma issue e suas subtasks."""
    try:
        main_issue =await get_issue(issue_id)
        data = {
            "summary": main_issue["fields"]["summary"],
            "description": main_issue["fields"].get("description", ""),
            "subtasks": []
        }

        url = f"{JIRA_URL}/rest/api/2/search?jql=parent={issue_id}"
        logger.info(
                    "Buscando informações sobre a subtasks da história %s.",
                    issue_id,
                )
        response = requests.get(url, headers=headers, verify=False, timeout=20)
        response.raise_for_status()
        if response.status_code == 200:
            issues = response.json()["issues"]
            for sub in issues:

                sub_key = sub["key"]
                data["subtasks"].append({
                    "key": sub_key,
                    "summary": sub["fields"]["summary"],
                    "description": sub["fields"].get("description", "")
                })

        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao buscar Jira '{issue_id}': {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
