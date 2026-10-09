class ResourceGraphClient:

    def list_workspaces(self):

        return [
            {
                "name": "workspace-example",
                "resource_group": "rg-security"
            }
        ]

    def list_virtual_machines(self):
        return []

    def list_subscriptions(self):
        return []
