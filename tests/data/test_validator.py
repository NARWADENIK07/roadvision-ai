from pathlib import Path

import pytest

from roadvision.data.exceptions import ValidationError
from roadvision.data.validator import (
    is_dataset_present,
    validate_dataset_directory,
)


def test_validate_existing_directory(tmp_path: Path) -> None:
    (tmp_path / "dummy.txt").write_text("dummy")

    assert validate_dataset_directory(tmp_path) == tmp_path


def test_validate_missing_directory() -> None:
    with pytest.raises(ValidationError):
        validate_dataset_directory("missing_directory")


def test_dataset_present(tmp_path: Path) -> None:
    (tmp_path / "dummy.txt").write_text("dummy")

    assert is_dataset_present(tmp_path)


def test_dataset_not_present(tmp_path: Path) -> None:
    missing = tmp_path / "missing"

    assert not is_dataset_present(missing)


def test_validate_empty_directory(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        validate_dataset_directory(tmp_path)
