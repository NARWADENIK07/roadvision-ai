from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetMetadata:
    """Metadata describing a dataset."""

    name: str
    version: str
    num_classes: int
    image_size: int
    archive_name: str
    dataset_directory: str


GTSRB_METADATA = DatasetMetadata(
    name="GTSRB",
    version="1.0",
    num_classes=43,
    image_size=224,
    archive_name="gtsrb.zip",
    dataset_directory="gtsrb",
)
