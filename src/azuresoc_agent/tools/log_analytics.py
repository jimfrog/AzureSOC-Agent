from azure.core.exceptions import HttpResponseError
from azure.monitor.query import LogsQueryClient
from azure.monitor.query import LogsQueryStatus

from azuresoc_agent.tools.azure_auth import get_credential


class LogAnalyticsClient:

    def __init__(self):

        self.client = LogsQueryClient(
            credential=get_credential()
        )

    def run_query(
        self,
        workspace_id,
        query,
        timespan=None
    ):
        """Runs a KQL query and returns a structured result dict.

        Returns a dict with keys:
          success: bool
          columns: list[str] (empty on failure)
          rows: list[list] (empty on failure)
          error: str (present only on failure)
        """

        try:

            response = self.client.query_workspace(
                workspace_id=workspace_id,
                query=query,
                timespan=timespan
            )

        except HttpResponseError as error:

            return {
                "success": False,
                "columns": [],
                "rows": [],
                "error": str(error)
            }

        if response.status == LogsQueryStatus.SUCCESS:
            tables = response.tables

        elif response.status == LogsQueryStatus.PARTIAL:
            tables = response.partial_data

        else:

            return {
                "success": False,
                "columns": [],
                "rows": [],
                "error": "Query returned no data."
            }

        if not tables:
            return {"success": True, "columns": [], "rows": []}

        table = tables[0]

        return {
            "success": True,
            "columns": list(table.columns),
            "rows": [list(row) for row in table.rows]
        }
