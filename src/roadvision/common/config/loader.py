"""
Configuration loader.

Responsible for loading YAML configuration files.
"""

from pathlib import Path
from typing import Any

import yaml

from roadvision.common.config.exceptions import ConfigurationError


def load_yaml_config(config_path: str | Path) -> dict[str, Any]:
    """
    Load a YAML configuration file.

    Args:
        config_path:
            Path to the YAML configuration file.

    Returns:
        Parsed configuration as a dictionary.

    Raises:
        ConfigurationError:
            If the configuration cannot be loaded.
    """

    config_path = Path(config_path)

    if not config_path.exists():
        raise ConfigurationError(f"Configuration file not found: {config_path}")

    try:
        with config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

    except yaml.YAMLError as error:
        raise ConfigurationError(f"Invalid YAML file: {config_path}") from error

    if not isinstance(config, dict):
        raise ConfigurationError(f"Configuration must be a dictionary: {config_path}")

    return config
