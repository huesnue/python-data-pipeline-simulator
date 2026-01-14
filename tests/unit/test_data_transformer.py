from src.data_transformer import DataTransformer

def test_data_transformer(sample_input):
    transformer = DataTransformer()
    data = {"name": "Alice"}
    transformed = transformer.transform(data)
    assert transformed == data
