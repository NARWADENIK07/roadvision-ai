from pathlib import Path
from zipfile import ZipFile

import pytest

from roadvision.data.exceptions import ExtractionError
from roadvision.data.extractor import extract_archive


def test_extract_archive(tmp_path: Path) -> None:
    archive = tmp_path / "sample.zip"

    with ZipFile(archive, "w") as zip_file:
        zip_file.writestr("hello.txt", "RoadVision AI")

    output = tmp_path / "output"

    extract_archive(archive, output)

    assert (output / "hello.txt").exists()
    assert (output / "hello.txt").read_text() == "RoadVision AI"


def test_extract_archive_rejects_path_traversal(tmp_path: Path) -> None:
    archive = tmp_path / "evil.zip"

    with ZipFile(archive, "w") as zip_file:
        zip_file.writestr("../../evil.txt", "malicious")

    destination = tmp_path / "output"

    with pytest.raises(ExtractionError):
        extract_archive(archive, destination)

    assert not destination.exists() or not any(destination.iterdir())
