from pathlib import Path
from unittest.mock import patch

from roadvision.data.downloader import download_dataset
from roadvision.data.source import GTSRB_SOURCE


def test_download_dataset(tmp_path: Path) -> None:
    expected = tmp_path / GTSRB_SOURCE.archive_name

    with patch(
        "roadvision.data.downloader.download_file",
        return_value=expected,
    ) as mock_download:
        result = download_dataset(GTSRB_SOURCE, tmp_path)

    mock_download.assert_called_once_with(
        GTSRB_SOURCE.url,
        expected,
    )

    assert result == expected
