class PipelineManager:
    def __init__(self, data_source, data_validator, data_transformer):
        self.data_source = data_source
        self.data_validator = data_validator
        self.data_transformer = data_transformer

    def run(self):
        try:
            # 1. Load data
            data = self.data_source.load()
            
            # 2. Validate data
            validated_data = self.data_validator.validate(data)
            
            # 3. Transform data
            transformed_data = self.data_transformer.transform(validated_data)
            
            # 4. Return final result
            return transformed_data
        except Exception as e:
            raise RuntimeError(f"Pipeline execution failed: {e}")
