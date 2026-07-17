"""Archive extraction utilities."""

from pathlib import Path
from zipfile import ZipFile

from loguru import logger


def extract_archive(
    archive_path: str | Path,
    destination: str | Path,
) -> Path:
    """Extract a ZIP archive."""

    archive_path = Path(archive_path)
    destination = Path(destination)

    logger.info("Extracting {}...", archive_path.name)

    destination.mkdir(parents=True, exist_ok=True)

    with ZipFile(archive_path) as archive:
        archive.extractall(destination)

    logger.success("Extraction completed.")

    return destination
