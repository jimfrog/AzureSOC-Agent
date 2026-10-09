from azuresoc_agent.agent.planner import Planner


class Orchestrator:

    def __init__(self):

        self.planner = Planner()

    def process(self, question):

        plan = self.planner.create_plan(question)

        if not plan:

            return {
                "success": False,
                "message": "Could not determine intent."
            }

        return {
            "success": True,
            "intent": plan["intent"],
            "query": plan["query"]
        }
