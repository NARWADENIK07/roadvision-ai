"""Dataset registry."""

from pathlib import Path

from roadvision.common.config import load_yaml_config
from roadvision.data.exceptions import DatasetNotFoundError
from roadvision.data.source import DatasetSource

_CONFIG_PATH = Path("configs/datasets.yaml")


def get_dataset_source(name: str) -> DatasetSource:
    """Return the configuration for a registered dataset."""

    config = load_yaml_config(_CONFIG_PATH)

    datasets = config.get("datasets", {})

    if name not in datasets:
        raise DatasetNotFoundError(f"Unknown dataset: {name}")

    dataset = datasets[name]

    return DatasetSource(
        name=dataset["name"],
        version=dataset["version"],
        url=dataset["url"],
        archive_name=dataset["archive_name"],
        dataset_directory=dataset["dataset_directory"],
        checksum=dataset.get("checksum"),
    )
