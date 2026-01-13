import json

class DataValidator:
    TYPE_MAP = {
        "string": str,
        "int": int,
        "float": float,
        "bool": bool
    }

    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        
    def _load_schema(self):
        with open(self.schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f) # Load schema from JSON file
        return schema
    
    def validate(self, data):
        schema = self._load_schema()
        
        for field, expected_type in schema.items():
            # 1. Is Field available?
            if field not in data:
                raise ValueError(f"Missing required field: '{field}'")
            
            # 2. Is Field of correct type?
            python_type = self.TYPE_MAP.get(expected_type)
            if python_type is None:
                raise ValueError(f"Unsupported type '{expected_type}' for field '{field}' in schema.")  
            
            if not isinstance(data[field], python_type):
                raise TypeError(f"Field '{field}' expected to be of type {expected_type}, "
                                f"got {type(data[field]).__name__}")
        
        # if all checks pass
        return data