import argparse
import logging
from src.pipeline_manager import PipelineManager
from src.config_loader import ConfigLoader

def setup_logger(level="INFO"):
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

def parse_args():
    parser = argparse.ArgumentParser(description="Run the modular data pipeline.")

    parser.add_argument("--input", help="Path to the input JSON file.")
    parser.add_argument("--schema", help="Path to the JSON schema file for validation.")
    parser.add_argument("--output", help="Path where the output JSON will be saved.")

    parser.add_argument(
        "--log-level",
        default=None,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Set the logging level."
    )

    parser.add_argument(
        "--config",
        help="Optional path to a YAML config file."
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # Load config if provided
    config = None
    if args.config:
        config = ConfigLoader(args.config).load()

    # Resolve values: CLI overrides config
    input_path = args.input or (config["pipeline"]["input"] if config else None)
    schema_path = args.schema or (config["pipeline"]["schema"] if config else None)
    output_path = args.output or (config["pipeline"]["output"] if config else None)
    log_level = args.log_level or (config["logging"]["level"] if config else "INFO")

    # Validate required values
    if not all([input_path, schema_path, output_path]):
        raise ValueError(
            "Missing required parameters. Provide either a config file or CLI arguments."
        )

    # Initialize logging AFTER resolving config
    setup_logger(log_level)

    pipeline = PipelineManager(
        input_path=input_path,
        schema_path=schema_path,
        output_path=output_path,
        log_level=log_level
    )

    pipeline.run()
    print("Pipeline finished successfully.")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()
