"""Dataset manager."""

import shutil
from pathlib import Path

from roadvision.data.downloader import download_dataset
from roadvision.data.exceptions import ValidationError
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

        external_dir = destination / "external"
        raw_dir = destination / "raw"

        external_dir.mkdir(parents=True, exist_ok=True)
        raw_dir.mkdir(parents=True, exist_ok=True)

        dataset_path = raw_dir / source.dataset_directory
        archive_path = external_dir / source.archive_name

        if dataset_path.exists():
            try:
                validate_dataset_directory(dataset_path)
                return dataset_path
            except ValidationError:
                shutil.rmtree(dataset_path)

        if not archive_path.exists():
            archive_path = download_dataset(source, external_dir)

        if source.checksum is not None:
            verify_checksum(archive_path, source.checksum)

        extract_archive(archive_path, dataset_path)
        validate_dataset_directory(dataset_path)

        return dataset_path
