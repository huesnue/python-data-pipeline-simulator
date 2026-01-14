from src.data_validator import DataValidator
from src.data_source import DataSource

def test_data_validator_valid(sample_input, sample_schema):
    data = DataSource(sample_input).load()
    validator = DataValidator(sample_schema)
    validated = validator.validate(data)
    assert validated == data
