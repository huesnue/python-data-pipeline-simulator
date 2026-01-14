import json
import csv
import os
import logging




class DataSource:
    def __init__(self, path: str):
        self.path = path
        self.logger = logging.getLogger(self.__class__.__name__)

    def load(self):
        self.logger.info(f"Loading data from {self.path}")
        
        # Check if file exists
        if not os.path.exists(self.path):
            self.logger.error(f"File not found: {self.path}")
            raise FileNotFoundError(f"The file at path '{self.path}' does not exist.")
        try:     
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.logger.info("Data loaded successfully")
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format: {e}")
            raise ValueError(f"Error decoding JSON from file '{self.path}': {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error while loading data: {e}")
        if not isinstance(data, dict):
            self.logger.error(f"Unexpected error: {e}")
            raise ValueError("Loaded JSON must be an object (Python dict).")     
        return data
        
