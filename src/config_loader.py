import yaml from pathlib
import Path

class ConfigLoader:
    def __init__(self, config_path="config/config.yaml"): 
        self.config_path = Path(config_path)
    
    def load(self):
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)