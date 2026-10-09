from azure.identity import DefaultAzureCredential


def get_credential():
    """
    Returns Azure credentials using:
      - Azure CLI
      - VS Code
      - Managed Identity
    """
    return DefaultAzureCredential()
