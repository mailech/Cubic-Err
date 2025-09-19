import pytest

def test_dataset_len():
    from ml_errors.dataloader import ToyDataset
    ds = ToyDataset([1, 2, 3])
    assert len(ds) == 3  # will fail (len returns 4)