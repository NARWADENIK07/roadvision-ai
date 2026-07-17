from roadvision.data.source import GTSRB_SOURCE


def test_gtsrb_source() -> None:
    assert GTSRB_SOURCE.archive_name == "gtsrb.zip"
    assert GTSRB_SOURCE.dataset_directory == "gtsrb"
    assert GTSRB_SOURCE.version == "1.0"
    assert GTSRB_SOURCE.checksum is None
