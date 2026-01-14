import pytest
import json
from pathlib import Path

@pytest.fixture
def sample_input(tmp_path):
    data = {"name": "Alice", "age": 30}
    file = tmp_path / "input.json"
    file.write_text(json.dumps(data))
    return file

@pytest.fixture
def sample_schema(tmp_path):
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["name", "age"]
    }
    file = tmp_path / "schema.json"
    file.write_text(json.dumps(schema))
    return file

@pytest.fixture
def output_path(tmp_path):
    return tmp_path / "output.json"
