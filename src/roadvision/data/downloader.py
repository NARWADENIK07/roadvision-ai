"""Dataset download utilities."""

from pathlib import Path

from loguru import logger

from roadvision.data.exceptions import DatasetError


def download_dataset(destination: str | Path) -> Path:
    """Prepare the dataset directory.

    The download implementation will be added in a later sprint.
    """

    destination = Path(destination)

    logger.info("Preparing dataset directory: {}", destination)

    destination.mkdir(parents=True, exist_ok=True)

    if not destination.exists():
        raise DatasetError(f"Failed to create dataset directory: {destination}")

    logger.success("Dataset directory is ready.")

    return destination
