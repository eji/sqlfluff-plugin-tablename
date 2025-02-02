from typing import Any, Dict, List, Type

from sqlfluff.core.config import load_config_resource
from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules import BaseRule

@hookimpl
def get_rules() -> List[Type[BaseRule]]:
    from sqlfluff_plugin_tablename.rules import Rule_TableName_L001  # noqa: F811

    return [Rule_TableName_L001]


@hookimpl
def load_default_config() -> Dict[str, Any]:
    """Loads the default configuration for the plugin."""
    return load_config_resource(
        package="sqlfluff_plugin_tablename",
        file_name="plugin_default_config.cfg",
    )


@hookimpl
def get_configs_info() -> Dict[str, Dict[str, Any]]:
    """Get rule config validations and descriptions."""
    return {
        "table_name": {"definition": "The table name to check for.", "type": "string"}
    }