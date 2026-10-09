class IntentRouter:

    @staticmethod
    def route(user_input):

        text = user_input.lower()

        if "linux" in text:
            return "linux_count"

        if "stopped" in text:
            return "stale_hosts"

        if "failed" in text:
            return "failed_logons"

        return None
