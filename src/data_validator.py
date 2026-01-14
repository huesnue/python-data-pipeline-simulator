import json
from pathlib import Path
import logging

from jsonschema import validate, ValidationError, SchemaError


class DataValidator:
    def __init__(self, schema_path: str):
        self.schema_path = Path(schema_path)
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def _load_schema(self):
        self.logger.info(f"Loading schema from {self.schema_path}")
        
        if not self.schema_path.exists():
            self.logger.error("Schema file not found")
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        try:
            with open(self.schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
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
        """
        Validate the given data against the JSON Schema.

        On success:
            - logs success
            - returns the original data (unchanged), as in the old implementation

        On failure:
            - logs the error
            - raises ValueError or RuntimeError
        """
        self.logger.info("Validating data")
        schema = self._load_schema()

        try:
            validate(instance=data, schema=schema)
            self.logger.info("Validation successful")
        except ValidationError as e:
            self.logger.error(f"Schema validation failed: {e.message}")
            raise ValueError(f"Schema validation failed: {e.message}")
        except SchemaError as e:
            self.logger.error(f"Invalid schema definition: {e.message}")
            raise ValueError(f"Invalid schema definition: {e.message}")
        except Exception as e:
            self.logger.error(f"Unexpected validation error: {e}")
            raise RuntimeError(f"Unexpected validation error: {e}")

        # Successful validation  → return data unchanged
        return data
