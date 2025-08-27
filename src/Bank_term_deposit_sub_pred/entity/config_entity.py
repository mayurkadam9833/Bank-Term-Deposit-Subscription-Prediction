from dataclasses import dataclass
from pathlib import Path

# config class for data ingestion step
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url: str
    local_data_file: Path 
    unzip_dir: Path

# config class for data validation step
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    unzip_data: Path
    STATUS_FILE: str
    all_schema: dict

# config class for data transformation step
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    target_col : str

# config class for model trainer 
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    model_name: str 
    target_col: str 
    n_estimators: int
    learning_rate: float

# config class for model evaluation 
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path 
    test_data_path: Path
    model_path: Path
    evaluation_file: Path
    target_col: str