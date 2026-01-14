import argparse
import logging
from src.pipeline_manager import PipelineManager

def setup_logger(level="INFO"):
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

def parse_args():
    parser = argparse.ArgumentParser(description="Run the modular data pipeline.")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input JSON file."
    )

    parser.add_argument(
        "--schema",
        required=True,
        help="Path to the JSON schema file for validation."
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path where the output JSON will be saved."
    )

    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Set the logging level."
    )

    return parser.parse_args()


def main():
    args = parse_args()
    setup_logger(args.log_level)

    pipeline = PipelineManager(
        input_path=args.input,
        schema_path=args.schema,
        output_path=args.output,
        log_level=args.log_level
    )

    pipeline.run()
    print("Pipeline finished successfully.")
    print(f"Output saved to: {args.output}")


if __name__ == "__main__":
    main()

