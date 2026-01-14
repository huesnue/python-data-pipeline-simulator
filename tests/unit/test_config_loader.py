import pytest
from src.config_loader import ConfigLoader

def test_config_loader_valid(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("pipeline:\n  input: file.json")

    loader = ConfigLoader(config_file)
    config = loader.load()

    assert config["pipeline"]["input"] == "file.json"

def test_config_loader_file_not_found(tmp_path):
    missing_file = tmp_path / "missing.yaml"
    loader = ConfigLoader(missing_file)

    with pytest.raises(FileNotFoundError):
        loader.load()

def test_config_loader_invalid_yaml(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("pipeline: [unclosed_list")

    loader = ConfigLoader(config_file)

    with pytest.raises(ValueError):
        loader.load()

def test_config_loader_io_error(tmp_path, monkeypatch):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("pipeline:\n  input: file.json")

    def fake_read_text(*args, **kwargs):
        raise OSError("disk error")

    monkeypatch.setattr(type(config_file), "read_text", fake_read_text)

    loader = ConfigLoader(config_file)

    with pytest.raises(RuntimeError):
        loader.load()
