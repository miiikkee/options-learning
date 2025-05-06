from src.data.fetch_data import fetch_raw_data

def test_fetch_raw_data_returns_not_none():
    assert fetch_raw_data() is not None

