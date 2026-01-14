import json
import logging
from pathlib import Path

class OutputWriter:
    def __init__(self, output_path: str):
        self.output_path = Path(output_path)
        self.logger = logging.getLogger(self.__class__.__name__)

    def save(self, data):
        self.logger.info(f"Saving output to {self.output_path}")

        # Ensure directory exists (modern, clean, Pythonic)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with self.output_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            self.logger.info("Output saved successfully")
        except Exception as e:
            self.logger.error(f"Failed to save output: {e}")
            raise RuntimeError(f"Could not save output: {e}")
