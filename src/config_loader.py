import yaml
from pathlib import Path
import logging

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.logger = logging.getLogger(self.__class__.__name__)

    def load(self):
        self.logger.info(f"Loading config from {self.config_path}")

        if not self.config_path.exists():
            self.logger.error("Config file not found")
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        try:
            content = self.config_path.read_text(encoding="utf-8")
            config = yaml.safe_load(content)
            self.logger.info("Config loaded successfully")
            return config
        except yaml.YAMLError as e:
            self.logger.error(f"Invalid YAML format: {e}")
            raise ValueError(f"Invalid YAML format: {e}")
        except Exception as e:
            self.logger.error(f"Error loading config: {e}")
            raise RuntimeError(f"Error loading config: {e}")
