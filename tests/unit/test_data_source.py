from src.data_source import DataSource

def test_data_source_load(sample_input):
    ds = DataSource(sample_input)
    data = ds.load()
    assert data["name"] == "Alice"
    assert data["age"] == 30
