"""Dataset manager."""

from pathlib import Path

from roadvision.data.downloader import download_dataset
from roadvision.data.extractor import extract_archive
from roadvision.data.integrity import verify_checksum
from roadvision.data.source import DatasetSource
from roadvision.data.validator import validate_dataset_directory


class DatasetManager:
    """Dataset manager."""

    def prepare(
        self,
        source: DatasetSource,
        destination: str | Path,
    ) -> Path:
        """Prepare a dataset."""

        destination = Path(destination)
        dataset_path = destination / source.dataset_directory

        if dataset_path.exists():
            validate_dataset_directory(dataset_path)
            return dataset_path

        archive_path = download_dataset(source, destination)

        if source.checksum is not None:
            verify_checksum(archive_path, source.checksum)

        extract_archive(archive_path, dataset_path)

        validate_dataset_directory(dataset_path)

        return dataset_path
