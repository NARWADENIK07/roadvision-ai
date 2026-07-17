"""Dataset lifecycle management."""

from pathlib import Path

from loguru import logger

from roadvision.data.downloader import download_dataset
from roadvision.data.validator import validate_dataset_directory


class DatasetManager:
    """Coordinate dataset preparation."""

    def prepare(self, destination: str | Path) -> Path:
        """Prepare a dataset for use."""

        logger.info("Preparing dataset...")

        dataset_path = download_dataset(destination)

        validate_dataset_directory(dataset_path)

        logger.success("Dataset preparation completed.")

        return dataset_path


def prepare_dataset(destination: str | Path) -> Path:
    """Convenience wrapper for dataset preparation."""

    manager = DatasetManager()
    return manager.prepare(destination)
