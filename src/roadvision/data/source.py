"""Dataset source definitions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetSource:
    """Information required to acquire a dataset."""

    name: str
    url: str
    archive_name: str
    dataset_directory: str


GTSRB_SOURCE = DatasetSource(
    name="GTSRB",
    url="",
    archive_name="gtsrb.zip",
    dataset_directory="gtsrb",
)
