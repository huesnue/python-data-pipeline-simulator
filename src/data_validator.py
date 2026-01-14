import json
import os
import logging

class DataValidator:
    TYPE_MAP = {
        "string": str,
        "int": int,
        "float": float,
        "bool": bool
    }

    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        self.logger = logging.getLogger(self.__class__.__name__)
    def _load_schema(self):
        self.logger.info(f"Loading schema from {self.schema_path}")
        
        if not os.path.exists(self.schema_path):
            self.logger.error("Schema file not found")
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")
        try:
            with open(self.schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f) # Load schema from JSON file
            self.logger.info("Schema loaded successfully")
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON schema format: {e}")
            raise ValueError(f"Invalid JSON schema format: {e}")
        except Exception as e:
            self.logger.error(f"Error loading schema: {e}")
            raise RuntimeError(f"Error loading schema: {e}")

        if not isinstance(schema, dict):
            self.logger.error("Schema must be a JSON object")
            raise ValueError("Schema must be a JSON object (Python dict).")
        
        return schema
    
    
    def validate(self, data):
        self.logger.info("Validating data")
        schema = self._load_schema()
        
        for field, expected_type in schema.items():
            # 1. Is Field available?
            if field not in data:
                self.logger.error(f"Missing required field: '{field}'")
                raise ValueError(f"Missing required field: '{field}'")
            
            # 2. Is Field of correct type?
            python_type = self.TYPE_MAP.get(expected_type)
            if python_type is None:
                self.logger.error(f"Unsupported type '{expected_type}' for field '{field}' in schema.")
                raise ValueError(f"Unsupported type '{expected_type}' for field '{field}' in schema.")  
            
            if not isinstance(data[field], python_type):
                self.logger.error(f"Type mismatch for field '{field}': expected {expected_type}, got {type(data[field]).__name__}")
                raise TypeError(f"Field '{field}' expected to be of type {expected_type}, "
                                f"got {type(data[field]).__name__}")
        
        # if all checks pass
        return data