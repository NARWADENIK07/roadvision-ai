from pathlib import Path

import pytest

from roadvision.data.inspector import inspect_dataset


def test_inspect_dataset_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        inspect_dataset(Path("dummy"))
