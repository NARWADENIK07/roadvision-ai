"""Download the RoadVision AI dataset."""

from roadvision.data import download_dataset


def main() -> None:
    """Run the dataset preparation script."""

    download_dataset("data/raw/gtsrb")


if __name__ == "__main__":
    main()
