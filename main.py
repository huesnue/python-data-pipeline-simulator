from src.logger_config import setup_logger
from src.data_source import DataSource
from src.data_validator import DataValidator
from src.data_transformer import DataTransformer
from src.output_writer import OutputWriter
from src.pipeline_manager import PipelineManager

def main():
    setup_logger()

    source = DataSource("data/input_sample.json")
    validator = DataValidator("data/schema.json")
    transformer = DataTransformer()
    output = OutputWriter("output/result.json")

    pipeline = PipelineManager(source, validator, transformer, output)
    result = pipeline.run()

    print("Pipeline finished successfully.")
    print("Output saved to output/result.json")

if __name__ == "__main__":
    main()
