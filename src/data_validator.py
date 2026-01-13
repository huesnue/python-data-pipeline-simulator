class DataValidator:
    def __init__(self, schema_path: str):
        self.schema_path = schema_path

    def validate(self, data):
        raise NotImplementedError("validate() must be implemented.")
