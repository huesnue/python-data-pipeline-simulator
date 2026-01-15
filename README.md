# Python Data Pipeline Simulator

![Coverage](coverage-badge.svg)

A modular, object-oriented data pipeline simulator built in Python.

This project demonstrates how real-world data pipelines are structured internally, including data ingestion, validation, transformation, and pipeline orchestration. It is part of my AI/MLOps engineering journey and reflects a focus on clean architecture, clear separation of concerns, and production-oriented engineering practices.

---

## 🚀 Project Overview

The Python Data Pipeline Simulator is a modular and extensible framework designed to demonstrate how real-world data pipelines are structured, validated, transformed, and orchestrated.  
It provides a clean, object-oriented architecture that mirrors modern data engineering and MLOps practices.

The project is built using Python and leverages industry-standard tools such as `pytest` for testing and GitHub Actions for continuous integration and coverage reporting.  
Its modular design makes it suitable for learning, experimentation, and future expansion into more advanced data workflows.

---

## Project Goals

- Provide a realistic and extensible simulation of a data pipeline architecture
- Demonstrate best practices in Python, object-oriented design, testing, and CI/CD
- Establish a solid foundation for future components (additional data sources, validators, transformers, writers)
- Offer a structured and maintainable codebase suitable for learning, experimentation, and further development

---

## 🧩 Features

- **Modular Architecture**  
  Each pipeline component (data source, validator, transformer, writer) is implemented as an independent, replaceable module.

- **Object-Oriented Design**  
  Clear separation of concerns with dedicated classes for each pipeline stage.

- **Data Validation Layer**  
  Ensures that incoming data meets structural and semantic requirements before processing.

- **Transformation Layer**  
  Applies configurable transformations to clean, enrich, or reshape the data.

- **Pipeline Orchestration**  
  A central `PipelineManager` coordinates the execution flow across all components.

- **Extensibility**  
  New data sources, validators, transformers, and writers can be added with minimal effort.

- **Logging Support**  
  Structured logging for better observability and debugging.

- **Automated Testing**  
  Comprehensive unit tests covering core pipeline functionality.

- **CI/CD Integration**  
  GitHub Actions pipeline running tests automatically on every push and pull request.

- **Coverage Reporting**  
  Automatic generation of a coverage badge to track test coverage over time.

---

## 🏗️ Architecture Overview

The pipeline is built around a clean, modular architecture that separates each processing stage into its own dedicated component. This design makes the system easy to extend, test, and maintain.

### Core Components

- **DataSource**  
  Responsible for loading raw input data (e.g., JSON, CSV).  
  Each data source implementation encapsulates its own loading logic.

- **DataValidator**  
  Ensures that incoming data meets structural and semantic requirements.  
  Validation failures are surfaced early to prevent downstream errors.

- **DataTransformer**  
  Applies transformations to clean, enrich, or reshape the data.  
  Transformers are fully customizable and can be chained or replaced.

- **PipelineManager**  
  Orchestrates the entire pipeline by coordinating the execution order:  
  `load → validate → transform → write`.  
  It acts as the central controller of the workflow.

- **Writer**  
  Handles output operations such as saving transformed data to disk or exporting it to other systems.

### Architectural Principles

- **Separation of Concerns**  
  Each component has a single, well-defined responsibility.

- **Extensibility**  
  New data sources, validators, transformers, or writers can be added without modifying existing code.

- **Loose Coupling**  
  Components interact through clear interfaces, making the system flexible and testable.

- **Testability**  
  The modular design enables isolated unit tests for each component.

### High-Level Data Flow
```
┌────────────┐
│ DataSource │
└──────┬─────┘
       │
       ▼
┌────────────┐
│ Validator  │
└──────┬─────┘
       │
       ▼
┌────────────┐
│ Transformer│
└──────┬─────┘
       │
       ▼
┌────────────┐
│   Writer   │
└────────────┘
```

The `PipelineManager` coordinates each step and ensures that data flows through the pipeline in a controlled and predictable manner.

---

## 📐 Technical Specifications

This section describes the responsibilities, inputs, outputs, and extension points of each core component in the pipeline.

### DataSource
**Responsibility:**  
Load raw input data from a specific source (e.g., JSON, CSV).

**Key Methods:**  
- `load()` — Reads and returns raw data.

**Input:**  
- File path or data source configuration.

**Output:**  
- Raw Python data structure (e.g., list, dict).

**Extensibility:**  
Implement custom subclasses for new formats such as APIs, databases, or streaming sources.

---

### DataValidator
**Responsibility:**  
Validate the structure and content of incoming data before processing.

**Key Methods:**  
- `validate(data)` — Raises an exception if validation fails.

**Input:**  
- Raw data from `DataSource`.

**Output:**  
- Validated data (unchanged) or an exception.

**Extensibility:**  
Add schema-based validators, type checkers, or domain-specific validation rules.

---

### DataTransformer
**Responsibility:**  
Apply transformations to clean, enrich, or reshape the data.

**Key Methods:**  
- `transform(data)` — Returns transformed data.

**Input:**  
- Validated data.

**Output:**  
- Transformed data.

**Extensibility:**  
Create custom transformers for feature engineering, normalization, filtering, or enrichment.

---

### Writer
**Responsibility:**  
Persist transformed data to a target destination (e.g., file, database, API).

**Key Methods:**  
- `write(data)` — Saves or exports the final output.

**Input:**  
- Transformed data.

**Output:**  
- Side effect: data written to disk or external system.

**Extensibility:**  
Implement writers for JSON, CSV, Parquet, SQL databases, or cloud storage.

---

### PipelineManager
**Responsibility:**  
Coordinate the entire pipeline execution flow.

**Key Methods:**  
- `run()` — Executes the full pipeline:  
  `load → validate → transform → write`

**Input:**  
- Instances of DataSource, DataValidator, DataTransformer, Writer.

**Output:**  
- Final processed data (optional return) and side effects from the writer.

**Extensibility:**  
Supports additional pipeline stages, branching logic, or multi-step workflows.

---

## 🔄 Pipeline Flow

The pipeline processes data through a sequence of well‑defined stages.  
Each stage is handled by a dedicated component, ensuring clarity, maintainability, and extensibility.

### Step-by-Step Flow

1. **Load**  
   The `DataSource` reads raw input data from a file or other source.

2. **Validate**  
   The `DataValidator` checks the structure and content of the data.  
   Invalid data triggers an exception before further processing.

3. **Transform**  
   The `DataTransformer` applies cleaning, enrichment, or reshaping operations.

4. **Write**  
   The `Writer` persists the transformed data to disk or another destination.

5. **Orchestrate**  
   The `PipelineManager` coordinates all steps and ensures a predictable execution order.

### Visual Overview

```
    Raw Data
       │
       ▼
┌─────────────┐
│  DataSource │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Validator  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Transformer │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Writer   │
└─────────────┘
```

### Execution Summary

The `PipelineManager` executes the full workflow:

load → validate → transform → write

This structured flow ensures that data is processed consistently and errors are caught early in the pipeline.

---

## 📦 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/huesnue/python-data-pipeline-simulator
cd python-data-pipeline-simulator
pip install -r requirements.txt

The project uses standard Python dependencies and does not require any additional setup.
```
---

## ▶️ Usage

The following example demonstrates how to initialize and run the pipeline using the core components.

```python
from pipeline_manager import PipelineManager
from data_source import DataSource
from data_validator import DataValidator
from data_transformer import DataTransformer
from writer import Writer

# Initialize pipeline components
source = DataSource("data/input_sample.json")
validator = DataValidator("data/schema.json")
transformer = DataTransformer()
writer = Writer("data/output.json")

# Create and run the pipeline
pipeline = PipelineManager(
    source=source,
    validator=validator,
    transformer=transformer,
    writer=writer
)

pipeline.run()

```
Running the script executes the full workflow:

load → validate → transform → write

---

## ⚙️ Configuration (optional)

The pipeline currently uses direct Python class initialization for all configuration parameters  
(e.g., file paths, schema locations, and output destinations).

A dedicated configuration layer is planned for future versions.  
This will allow the pipeline to be configured using:

- JSON or YAML configuration files  
- Environment variables  
- CLI arguments  
- Centralized settings for data sources, validators, transformers, and writers  

This design will make the pipeline easier to customize, automate, and integrate into larger ML/MLOps workflows.

---

## 🧪 Tests & Coverage

The project includes a growing suite of unit tests that validate the core functionality of each pipeline component.  
Tests are designed to be isolated, deterministic, and easy to extend as new features are added.

### Running Tests

Use the following command to execute all tests:

```bash
pytest
```

Test Structure
Tests are organized by component:

Test Structure
Tests are organized by component:

tests/
│
├── test_data_source.py
├── test_data_validator.py
├── test_data_transformer.py
├── test_pipeline_manager.py
└── ...

Each test module focuses on a single responsibility, mirroring the structure of the source code.

Coverage Reporting
Test coverage is automatically measured and published through GitHub Actions.
A coverage badge is generated on each successful run and displayed in the README.

To generate a local coverage report:
```bash
pytest --cov=src --cov-report=term-missing
```

This provides a detailed breakdown of which lines and branches are covered.

CI Integration
All tests run automatically on every push and pull request.
If any test fails, the CI pipeline blocks the merge to ensure code quality and stability.

---

## 🔁 CI/CD

The project includes a GitHub Actions workflow that automatically runs tests and generates a coverage report on every push and pull request. This ensures consistent code quality and prevents regressions.

### What the CI Pipeline Does

- Installs project dependencies  
- Runs the full test suite using `pytest`  
- Measures code coverage  
- Generates and updates the coverage badge  
- Blocks merges if tests fail  

### Workflow Location

The CI configuration is stored in:
.github/workflows/tests.yml


### Benefits

- Ensures reliable and repeatable test execution  
- Provides immediate feedback on code changes  
- Maintains high code quality through automated checks  
- Makes the project suitable for professional engineering workflows  

---

## 📂 Project Structure

The project follows a clean and modular layout that mirrors the architecture of the pipeline.  
Each component is placed in its own file to ensure clarity, maintainability, and extensibility.

```
python-data-pipeline-simulator/
│
├── src/
│   ├── data_source.py         # Loads raw input data   
│   ├── data_validator.py      # Validates structure and content
│   ├── data_transformer.py    # Applies transformations
│   ├── pipeline_manager.py    # Orchestrates the pipeline flow
│   ├── writer.py              # Writes output data
│   └── __init__.py
│
├── scripts/
│   └── generate_coverage_badge.py   # Script used by CI to generate the
coverage badge
│
├── config/
│   ├── pipeline_config.yaml    # Future configuration file (optional)
│   └── logging.yaml             # Logging configuration (optional)
│
├── tests/
│   ├── test_data_source.py
│   ├── test_data_validator.py
│   ├── test_data_transformer.py
│   └── test_pipeline_manager.py
│   └── ...
│
├── data/
│   ├── input_sample.json       # Example input data
│   ├── schema.json              # Example validation schema
│   └── output.json              # Example output file
│
├── .github/
│   └── workflows/
│       └── tests.yml            # CI pipeline for tests & coverage
│
├── requirements.txt
├── README.md
└── coverage-badge.svg
```

---

## 🗺️ Roadmap

The project is designed to grow over time.  
Future enhancements will focus on expanding functionality, improving configurability, and enabling more advanced data‑engineering and MLOps workflows.

### Planned Enhancements

- **Additional Data Sources**  
  Support for APIs, SQL databases, cloud storage, and streaming inputs.

- **Schema-Based Validation**  
  Integration of JSON Schema or Pydantic for more robust validation.

- **Advanced Transformation Layer**  
  Support for chained transformations, reusable transformation blocks, and domain-specific logic.

- **Config-Driven Pipeline**  
  YAML/JSON configuration files to define pipeline components, paths, and parameters.

- **CLI Interface**  
  A command-line tool to run pipelines, validate configs, and inspect outputs.

- **Improved Logging**  
  Structured logging with configurable log levels and optional file output.

- **Dockerization**  
  Containerized execution for reproducibility and deployment.

- **Pipeline Visualization**  
  Graph-based visualization of pipeline stages and data flow.

- **Integration Tests**  
  End-to-end tests covering full pipeline execution.

### Long-Term Ideas

- **Plugin System**  
  Allow users to register custom components dynamically.

- **Web Dashboard**  
  A lightweight UI to run pipelines, inspect logs, and view results.

- **MLOps Extensions**  
  Hooks for model training, feature engineering, and monitoring.

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, distribute, and integrate the code in personal or commercial projects, provided that the original license notice is included.

See the `LICENSE` file for full details.

