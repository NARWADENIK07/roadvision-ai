from pathlib import Path
from unittest.mock import patch

from roadvision.data.manager import DatasetManager
from roadvision.data.source import GTSRB_SOURCE


def test_prepare_existing_dataset(tmp_path: Path) -> None:
    dataset = tmp_path / GTSRB_SOURCE.dataset_directory
    dataset.mkdir(parents=True)

    manager = DatasetManager()

    with patch(
        "roadvision.data.manager.validate_dataset_directory",
    ) as mock_validate:
        result = manager.prepare(GTSRB_SOURCE, tmp_path)

    mock_validate.assert_called_once_with(dataset)
    assert result == dataset


def test_prepare_download_dataset(tmp_path: Path) -> None:
    manager = DatasetManager()

    archive = tmp_path / GTSRB_SOURCE.archive_name
    dataset = tmp_path / GTSRB_SOURCE.dataset_directory

    with (
        patch(
            "roadvision.data.manager.download_dataset",
            return_value=archive,
        ) as mock_download,
        patch("roadvision.data.manager.extract_archive") as mock_extract,
        patch("roadvision.data.manager.validate_dataset_directory") as mock_validate,
    ):
        result = manager.prepare(GTSRB_SOURCE, tmp_path)

    mock_download.assert_called_once()
    mock_extract.assert_called_once_with(archive, dataset)
    mock_validate.assert_called_once_with(dataset)

    assert result == dataset
