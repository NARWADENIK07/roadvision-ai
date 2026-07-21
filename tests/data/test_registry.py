from pytest import raises

from roadvision.data.exceptions import DatasetNotFoundError
from roadvision.data.registry import get_dataset_source


def test_get_dataset_source() -> None:
    source = get_dataset_source("gtsrb")

    assert source.name == "GTSRB"
    assert source.archive_name == "gtsrb.zip"


def test_unknown_dataset() -> None:
    with raises(DatasetNotFoundError):
        get_dataset_source("unknown")
