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