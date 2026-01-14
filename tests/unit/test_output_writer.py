from src.output_writer import OutputWriter
import json

def test_output_writer(output_path):
    writer = OutputWriter(output_path)
    data = {"x": 1}
    writer.save(data)

    saved = json.loads(output_path.read_text())
    assert saved["x"] == 1
