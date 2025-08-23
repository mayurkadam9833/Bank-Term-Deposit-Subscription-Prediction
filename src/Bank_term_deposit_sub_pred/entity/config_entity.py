from dataclasses import dataclass
from pathlib import Path

# config class for data ingestion setp
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url: str
    local_data_file: Path 
    unzip_dir: Path