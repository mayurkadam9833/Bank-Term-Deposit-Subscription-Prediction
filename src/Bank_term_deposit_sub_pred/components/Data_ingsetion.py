import os
import zipfile
from urllib.request import urlretrieve
from src.Bank_term_deposit_sub_pred.logging import logger
from src.Bank_term_deposit_sub_pred.utils.common import get_size
from src.Bank_term_deposit_sub_pred.entity.config_entity import DataIngestionConfig

"""
class for data ingestion contained methods 
-> download file
-> extract file 
"""
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    # method for download file
    def Download_file(self):
        try:
            # download file from source url if file not exists
            if not os.path.exists(self.config.local_data_file):
                filename,header=urlretrieve(
                    url=self.config.source_url,  # define source data url
                    filename=self.config.local_data_file 
                )
                logger.info(f"{filename} download sucessfully from following header:\n{header}")

            # if file is exists then return file size
            else:
                logger.info(f"{self.config.local_data_file} is already exists of size {get_size(filename)}") 

        except Exception as e:
            raise e

    # method for unzip file in directory 
    def extract_file(self):
        #create unzip file path
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        # load file & extract
        with zipfile.ZipFile(self.config.local_data_file,"r")as zipref:
            zipref.extractall(unzip_path) 

    

