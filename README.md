# AzureSOC-Agent

Natural language operations for:

- Microsoft Sentinel
- Log Analytics
- KQL
- Azure Data Explorer
- Defender XDR
- Entra ID

## Install

pip install -r requirements.txt

## Configure

Set your Log Analytics workspace ID in one of two places:

- `AZURE_LOG_ANALYTICS_WORKSPACE_ID` in `.env` (copy from `.env.example`), or
- `azure.default_workspace` in `config/settings.yaml`

Azure credentials are resolved via `DefaultAzureCredential` (Azure CLI, VS Code, Managed Identity, etc.).

## Run

python src/azuresoc_agent/cli/main.py

## Example Questions

How many Linux systems are reporting?

Show systems that stopped reporting.

Show failed logons.
