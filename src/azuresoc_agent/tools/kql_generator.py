QUERIES = {

    "linux_count": """
Heartbeat
| where OSType == "Linux"
| summarize Count=count()
""",

    "stale_hosts": """
Heartbeat
| summarize LastSeen=max(TimeGenerated) by Computer
| where LastSeen < ago(1d)
""",

    "failed_logons": """
SecurityEvent
| where EventID == 4625
| summarize Count=count() by Account
| order by Count desc
"""
}


def build_query(intent: str) -> str:
    return QUERIES.get(intent, "")
