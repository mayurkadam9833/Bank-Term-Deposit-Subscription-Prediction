import pandas as pd
from src.Bank_term_deposit_sub_pred.logging import logger
from src.Bank_term_deposit_sub_pred.entity.config_entity import DataValidationConfig

"""
DataValidation class contain schema validation methods which will validated schema of download data with define schema
"""
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config 
    
    # method to validate schema
    def schema_validation(self):
        try:
            schema_validation = True
            # read data 
            data=pd.read_csv(self.config.unzip_data,sep=";")
            all_cols=list(data.columns)
            all_schema=self.config.all_schema.keys()

            # loop throgh to validate each column if not match validation passed-> true and else-> False
            for col in all_cols:
                if col == "y":
                    continue
                if col not in all_schema:
                    schema_validation=False
                    logger.info(f"{col} is not present in defined schema, check this column.")
                    break
                
                with open(self.config.STATUS_FILE,"w")as file:
                        file.write(f"schema status: {schema_validation}")
            # return schema validation status 
            return schema_validation
        # raise exception
        except Exception as e:
            raise e