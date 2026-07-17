"""Dataset validation utilities."""

from pathlib import Path

from roadvision.data.exceptions import ValidationError


def validate_dataset_directory(dataset_path: str | Path) -> Path:
    """Validate a dataset directory."""

    path = Path(dataset_path)

    if not path.exists():
        raise ValidationError(f"Dataset directory not found: {path}")

    if not path.is_dir():
        raise ValidationError(f"Expected directory: {path}")

    return path


def is_dataset_present(dataset_path: str | Path) -> bool:
    """Return True if the dataset directory exists."""

    return Path(dataset_path).exists()
