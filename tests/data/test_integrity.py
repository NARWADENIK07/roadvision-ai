from hashlib import sha256
from pathlib import Path

import pytest

from roadvision.data.exceptions import ChecksumMismatchError
from roadvision.data.integrity import (
    calculate_sha256,
    verify_checksum,
)


def test_calculate_sha256(tmp_path: Path) -> None:
    file = tmp_path / "sample.txt"
    file.write_text("RoadVision AI")

    expected = sha256(b"RoadVision AI").hexdigest()

    assert calculate_sha256(file) == expected


def test_verify_checksum(tmp_path: Path) -> None:
    file = tmp_path / "sample.txt"
    file.write_text("RoadVision AI")

    expected = sha256(b"RoadVision AI").hexdigest()

    # Should not raise an exception.
    verify_checksum(file, expected)


def test_verify_checksum_invalid(tmp_path: Path) -> None:
    file = tmp_path / "sample.txt"
    file.write_text("RoadVision AI")

    with pytest.raises(ChecksumMismatchError):
        verify_checksum(file, "invalid_checksum")
