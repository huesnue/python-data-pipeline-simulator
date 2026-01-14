from src.pipeline_manager import PipelineManager

def test_pipeline_end_to_end(sample_input, sample_schema, output_path):
    pipeline = PipelineManager(
        input_path=sample_input,
        schema_path=sample_schema,
        output_path=output_path,
        log_level="INFO"
    )

    result = pipeline.run()

    assert result["name"] == "Alice"
    assert output_path.exists()
