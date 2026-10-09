from azuresoc_agent.agent.intent_router import IntentRouter
from azuresoc_agent.tools.kql_generator import build_query


class Planner:

    def create_plan(self, question):

        intent = IntentRouter.route(question)

        if not intent:
            return None

        query = build_query(intent)

        return {
            "intent": intent,
            "query": query
        }
