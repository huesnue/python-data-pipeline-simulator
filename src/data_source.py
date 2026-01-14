import json
import csv
import os

class DataSource:
    def __init__(self, path: str):
        self.path = path

    def load(self):
        # Check if file exists
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"The file at path '{self.path}' does not exist.")
        
        try:     
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file '{self.path}': {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error while loading data: {e}")
        if not isinstance(data, dict):
            raise ValueError("Loaded JSON must be an object (Python dict).")     
        return data
        
