import logging
from src.data_source import DataSource
from src.data_validator import DataValidator
from src.data_transformer import DataTransformer
from src.output_writer import OutputWriter
class PipelineManager:
    def __init__(self, input_path, schema_path, output_path, log_level="INFO"):
        self.data_source = DataSource(input_path)
        self.data_validator = DataValidator(schema_path)
        self.data_transformer = DataTransformer()
        self.output_writer = OutputWriter(output_path)
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        self.logger.info("Starting pipeline execution")
        try:
            # 1. Load data
            data = self.data_source.load()
            
            # 2. Validate data
            validated_data = self.data_validator.validate(data)
            
            # 3. Transform data
            transformed_data = self.data_transformer.transform(validated_data)
            self.output_writer.save(transformed_data)
            
            self.logger.info("Pipeline execution completed successfully")
            # 4. Return final result
            return transformed_data
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {e}")
            raise RuntimeError(f"Pipeline execution failed: {e}")
