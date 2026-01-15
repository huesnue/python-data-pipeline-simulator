# Python Data Pipeline Simulator

![Coverage](coverage-badge.svg)

A modular, object-oriented data pipeline simulator built in Python.

This project demonstrates how real-world data pipelines are structured internally, including data ingestion, validation, transformation, and pipeline orchestration. It is part of my AI/MLOps engineering journey and reflects a focus on clean architecture, clear separation of concerns, and production-oriented engineering practices.

---

## 🚀 Project Overview

Modern machine learning systems rely on robust, maintainable, and well‑structured data pipelines.
This project simulates the core components of such pipelines using Python and object‑oriented design principles.

The simulator models how real-world data pipelines ingest, validate, transform, and route data through clearly defined processing stages. It serves as a foundation for exploring clean architecture, extensibility, and production‑oriented engineering practices within the context of AI/MLOps workflows. 

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

    Raw Data
       │
       ▼
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


---

## 📁 Project Structure

```
python-data-pipeline-simulator/
│
├── src/
│   ├── data_source.py
│   ├── data_validator.py
│   ├── data_transformer.py
│   ├── pipeline_manager.py
│   └── __init__.py
│
├── data/
│   ├── input_sample.json
│   ├── input_sample.csv
│   └── schema.json
│
├── tests/
│   ├── test_data_source.py
│   ├── test_data_validator.py
│   ├── test_data_transformer.py
│   └── test_pipeline_manager.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── docs/
│   ├── architecture_diagram.png
│   ├── pipeline_flow.md
│   └── class_design.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3.x  
- OOP design patterns  
- JSON & CSV handling  
- Logging  
- (Optional) Pandas, NumPy  
- (Optional) Pytest for unit tests  

---

## ▶️ How to Run

1. Clone the repository:

```
git clone `https://github.com/huesnue/python-data-pipeline-simulator.git` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2Fhuesnue%2Fpython-data-pipeline-simulator.git")
cd python-data-pipeline-simulator
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the pipeline:

```python
from src.pipeline_manager import PipelineManager
from src.data_source import DataSource
from src.data_validator import DataValidator
from src.data_transformer import DataTransformer

pipeline = PipelineManager(
    source=DataSource("data/input_sample.json"),
    validator=DataValidator("data/schema.json"),
    transformer=DataTransformer()
)

pipeline.run()
```

---

## 📐 Architecture

The pipeline follows a clean, modular architecture:

```
DataSource → DataValidator → DataTransformer → PipelineManager
```

Each component is isolated and testable.

---

## 📚 What I Learned

- Designing maintainable Python modules  
- Applying OOP principles to real-world data workflows  
- Implementing schema validation and transformation logic  
- Structuring ML/MLOps‑ready pipelines  
- Writing clean, extensible, production‑style code  

---

## 🔮 Future Extensions

- Add CLI interface  
- Add database connectors (SQL, NoSQL)  
- Add parallel processing  
- Add unit tests for all components  
- Add integration with cloud storage (S3, GCS, Azure Blob)  

---

## 📄 License

MIT License

