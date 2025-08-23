from src.Bank_term_deposit_sub_pred.components.Data_ingsetion import DataIngestion
from src.Bank_term_deposit_sub_pred.config.configuration import ConfigManager
from src.Bank_term_deposit_sub_pred.logging import logger


"""
This Data Ingestion Pipeline class called function Download_file, Extract_file
which will download data file, unzip data file & store into defined path
"""
class DataIngestionPipeline:
    def __init__(self):
        pass 
    # Data ingestion pipeline
    def main(self):
        config=ConfigManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingsetion=DataIngestion(config=data_ingestion_config)
        data_ingsetion.Download_file() 
        data_ingsetion.Extract_file()

