# Python Data Pipeline Simulator

A modular, object-oriented data pipeline simulator built in Python.  
This project demonstrates how real-world data pipelines are structured internally, including data ingestion, validation, transformation, and pipeline orchestration.  
It is part of my AI/MLOps engineering training and showcases clean architecture, OOP principles, and production-ready code structure.

---

## 🚀 Project Overview

Modern machine learning systems rely on robust, maintainable data pipelines.  
This project simulates the core components of such pipelines using Python and object-oriented design.

The goal is to demonstrate:

- Clean and modular software architecture  
- Separation of concerns across pipeline stages  
- Error handling and validation logic  
- Extensibility for future ML/MLOps workflows  

---

## 🧩 Features

- **Data Ingestion**  
  Load JSON or CSV files through a dedicated `DataSource` class.

- **Data Validation**  
  Schema checks, type validation, and missing-value detection.

- **Data Transformation**  
  Cleaning, feature extraction, and transformation logic.

- **Pipeline Orchestration**  
  A `PipelineManager` class coordinates all steps with logging and error handling.

- **Extensible Architecture**  
  Easy to add new validators, transformers, or data sources.

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

