"""Prepare the GTSRB dataset."""

from pathlib import Path

from roadvision.data.manager import DatasetManager
from roadvision.data.registry import get_dataset_source


def main() -> None:
    """Prepare the dataset."""

    manager = DatasetManager()

    dataset_path = manager.prepare(
        source=get_dataset_source("gtsrb"),
        destination=Path("data/raw"),
    )

    print(f"Dataset ready: {dataset_path}")


if __name__ == "__main__":
    main()
