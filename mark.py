import pytest

@pytest.mark.slow
def test_data_processing():
    # Simulate a long-running test
    assert True

@pytest.mark.fast
def test_addition():
    assert 1 + 1 == 2
