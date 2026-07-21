from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetSource:
    """Information required to acquire a dataset."""

    name: str
    version: str
    url: str
    archive_name: str
    dataset_directory: str
    checksum: str | None = None
