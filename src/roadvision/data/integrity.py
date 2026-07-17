"""Dataset integrity verification."""

from hashlib import sha256
from pathlib import Path

CHUNK_SIZE = 8192


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
) -> bool:
    """Verify the SHA-256 checksum."""

    return calculate_sha256(file_path) == expected_checksum
