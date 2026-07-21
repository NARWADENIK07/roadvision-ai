"""Custom exceptions for the data module."""


class DatasetError(Exception):
    """Base exception for all dataset-related errors."""


class DownloadError(DatasetError):
    """Raised when dataset download fails."""


class ExtractionError(DatasetError):
    """Raised when archive extraction fails."""


class ChecksumMismatchError(DatasetError):
    """Raised when checksum verification fails."""


class ValidationError(DatasetError):
    """Raised when dataset validation fails."""


class DatasetNotFoundError(Exception):
    """Raised when a dataset is not registered."""
