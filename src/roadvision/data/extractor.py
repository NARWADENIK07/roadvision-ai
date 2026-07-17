"""Archive extraction utilities."""

from pathlib import Path
from zipfile import ZipFile

from roadvision.data.exceptions import ExtractionError


def extract_archive(
    archive_path: str | Path,
    destination: str | Path,
) -> Path:
    """Extract a ZIP archive safely."""

    archive_path = Path(archive_path)
    destination = Path(destination)

    destination.mkdir(parents=True, exist_ok=True)

    with ZipFile(archive_path) as archive:
        for member in archive.infolist():
            target_path = (destination / member.filename).resolve()

            if not target_path.is_relative_to(destination.resolve()):
                raise ExtractionError(f"Unsafe archive member: {member.filename}")

        archive.extractall(destination)

    return destination
