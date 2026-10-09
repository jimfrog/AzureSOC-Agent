import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_CONFIG_PATH = _REPO_ROOT / "config" / "settings.yaml"


def load_settings():
    """Loads config/settings.yaml as a dict."""

    if not _CONFIG_PATH.exists():
        return {}

    with open(_CONFIG_PATH, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file) or {}


def get_workspace_id():
    """Resolves the Log Analytics workspace ID.

    Checks the AZURE_LOG_ANALYTICS_WORKSPACE_ID environment variable first,
    then falls back to azure.default_workspace in config/settings.yaml.
    """

    env_value = os.getenv("AZURE_LOG_ANALYTICS_WORKSPACE_ID")

    if env_value:
        return env_value

    settings = load_settings()

    return settings.get("azure", {}).get("default_workspace", "")
