from pathlib import Path

import pytest

from roadvision.common.config import load_yaml_config
from roadvision.common.config.exceptions import ConfigurationError


def test_load_valid_yaml(tmp_path: Path) -> None:
    """A valid YAML configuration should load successfully."""

    config_file = tmp_path / "train.yaml"

    config_file.write_text(
        """
training:
  batch_size: 32
  epochs: 10
""",
        encoding="utf-8",
    )

    config = load_yaml_config(config_file)

    assert config["training"]["batch_size"] == 32
    assert config["training"]["epochs"] == 10


def test_missing_file() -> None:
    """Loading a missing file should raise ConfigurationError."""

    with pytest.raises(ConfigurationError):
        load_yaml_config("does_not_exist.yaml")


def test_invalid_yaml(tmp_path: Path) -> None:
    """Invalid YAML should raise ConfigurationError."""

    config_file = tmp_path / "invalid.yaml"

    config_file.write_text(
        """
training:
  batch_size: [1,2,
""",
        encoding="utf-8",
    )

    with pytest.raises(ConfigurationError):
        load_yaml_config(config_file)


def test_top_level_is_not_dictionary(tmp_path: Path) -> None:
    """Top-level YAML must be a dictionary."""

    config_file = tmp_path / "list.yaml"

    config_file.write_text(
        """
- one
- two
""",
        encoding="utf-8",
    )

    with pytest.raises(ConfigurationError):
        load_yaml_config(config_file)
