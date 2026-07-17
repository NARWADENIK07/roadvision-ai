"""Dataset downloader."""

from pathlib import Path

import requests
from loguru import logger
from requests import RequestException
from tqdm import tqdm

from roadvision.data.exceptions import DownloadError
from roadvision.data.source import DatasetSource

CHUNK_SIZE = 8192


def download_file(url: str, destination: Path) -> Path:
    """Download a file from a URL."""

    logger.info("Downloading {}...", destination.name)

    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
    except RequestException as exc:
        raise DownloadError(f"Failed to download: {url}") from exc

    total_size = int(response.headers.get("content-length", 0))

    destination.parent.mkdir(parents=True, exist_ok=True)

    with (
        destination.open("wb") as file,
        tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            desc=destination.name,
        ) as progress,
    ):
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                file.write(chunk)
                progress.update(len(chunk))

    logger.success("Downloaded {}", destination)

    return destination


def download_dataset(
    source: DatasetSource,
    download_dir: str | Path,
) -> Path:
    """Download a dataset archive."""

    download_dir = Path(download_dir)
    download_dir.mkdir(parents=True, exist_ok=True)

    archive_path = download_dir / source.archive_name

    return download_file(source.url, archive_path)
