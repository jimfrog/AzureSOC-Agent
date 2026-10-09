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

        response = self.client.query_workspace(
            workspace_id=workspace_id,
            query=query,
            timespan=timespan
        )

        if response.status == LogsQueryStatus.SUCCESS:

            records = []

            for table in response.tables:

                for row in table.rows:

                    records.append(row)

            return records

        return []
