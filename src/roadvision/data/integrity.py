"""Dataset integrity checks."""

from hashlib import sha256
from pathlib import Path

from roadvision.data.exceptions import ChecksumMismatchError

CHUNK_SIZE = 8192


def verify_dataset(dataset_path: str | Path) -> bool:
    """Verify dataset integrity.

    Implementation will be added in a later sprint.
    """
    raise NotImplementedError


def calculate_sha256(file_path: str | Path) -> str:
    """Calculate the SHA-256 hash of a file."""

    file_path = Path(file_path)

    digest = sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(CHUNK_SIZE):
            digest.update(chunk)

    return digest.hexdigest()


def verify_checksum(
    file_path: str | Path,
    expected_checksum: str,
) -> None:
    """Verify the SHA-256 checksum."""

    actual_checksum = calculate_sha256(file_path)

    if actual_checksum != expected_checksum:
        raise ChecksumMismatchError(f"Checksum mismatch for: {file_path}")
