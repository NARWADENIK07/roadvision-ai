"""Dataset source definitions."""

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


GTSRB_SOURCE = DatasetSource(
    name="GTSRB",
    version="1.0",
    url="",
    archive_name="gtsrb.zip",
    dataset_directory="gtsrb",
    checksum=None,
)
