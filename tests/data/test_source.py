from roadvision.data.registry import get_dataset_source


def test_registry_returns_gtsrb() -> None:
    source = get_dataset_source("gtsrb")

    assert source.archive_name == "gtsrb.zip"
    assert source.dataset_directory == "gtsrb"
    assert source.version == "1.0"
