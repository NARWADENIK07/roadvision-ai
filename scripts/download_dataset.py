"""Prepare the RoadVision AI dataset."""

from roadvision.data import prepare_dataset


def main() -> None:
    """Run the dataset preparation script."""

    prepare_dataset("data/raw/gtsrb")


if __name__ == "__main__":
    main()
