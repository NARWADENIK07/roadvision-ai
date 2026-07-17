from pathlib import Path

from roadvision.data.manager import prepare_dataset


def test_prepare_dataset(tmp_path: Path) -> None:
    dataset_path = prepare_dataset(tmp_path)

    assert dataset_path.exists()
    assert dataset_path.is_dir()
