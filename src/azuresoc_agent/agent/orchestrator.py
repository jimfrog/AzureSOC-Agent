from azuresoc_agent.agent.planner import Planner
from azuresoc_agent.config import get_workspace_id
from azuresoc_agent.tools.log_analytics import LogAnalyticsClient


class Orchestrator:

    def __init__(self):

        self.planner = Planner()
        self.log_analytics = LogAnalyticsClient()

    def process(self, question):

        plan = self.planner.create_plan(question)

        if not plan:

            return {
                "success": False,
                "message": "Could not determine intent."
            }

        workspace_id = get_workspace_id()

        if not workspace_id:

            return {
                "success": False,
                "intent": plan["intent"],
                "query": plan["query"],
                "message": (
                    "No Log Analytics workspace configured. Set the "
                    "AZURE_LOG_ANALYTICS_WORKSPACE_ID environment variable or "
                    "azure.default_workspace in config/settings.yaml."
                )
            }

        result = self.log_analytics.run_query(
            workspace_id=workspace_id,
            query=plan["query"]
        )

        if not result["success"]:

            return {
                "success": False,
                "intent": plan["intent"],
                "query": plan["query"],
                "message": result.get("error", "Query failed.")
            }

        return {
            "success": True,
            "intent": plan["intent"],
            "query": plan["query"],
            "columns": result["columns"],
            "rows": result["rows"]
        }
