from pathlib import Path
from unittest.mock import patch

import pytest
import requests

from roadvision.data.downloader import download_dataset, download_file
from roadvision.data.exceptions import DownloadError
from roadvision.data.registry import get_dataset_source

SOURCE = get_dataset_source("gtsrb")


def test_download_dataset(tmp_path: Path) -> None:
    expected = tmp_path / SOURCE.archive_name

    with patch(
        "roadvision.data.downloader.download_file",
        return_value=expected,
    ) as mock_download:
        result = download_dataset(SOURCE, tmp_path)

    mock_download.assert_called_once_with(
        SOURCE.url,
        expected,
    )

    assert result == expected


@patch("roadvision.data.downloader.requests.get")
def test_download_file_connection_error(mock_get) -> None:
    mock_get.side_effect = requests.exceptions.ConnectionError

    with pytest.raises(DownloadError):
        download_file(
            "https://example.com/file.zip",
            Path("dummy.zip"),
        )


@patch("roadvision.data.downloader.requests.get")
def test_download_file_http_error(mock_get) -> None:
    response = mock_get.return_value
    response.raise_for_status.side_effect = requests.exceptions.HTTPError

    with pytest.raises(DownloadError):
        download_file(
            "https://example.com/file.zip",
            Path("dummy.zip"),
        )
