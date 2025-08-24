from src.Bank_term_deposit_sub_pred.config.configuration import ConfigManager
from src.Bank_term_deposit_sub_pred.components.Data_validation import DataValidation


"""
This Data Validation Pipeline class called function schema validation
which will validated dataset schema if match return True and if not match return False
"""
class DataValidationPipeline:
    def __init__(self):
         pass 
    # Data validation pipeline
    def main(self):
         config=ConfigManager()
         data_validation_config=config.get_data_validation_config()
         data_validation=DataValidation(config=data_validation_config)
         data_validation.schema_validation()