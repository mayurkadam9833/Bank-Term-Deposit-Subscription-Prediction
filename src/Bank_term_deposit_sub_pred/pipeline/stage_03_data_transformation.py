from src.Bank_term_deposit_sub_pred.config.configuration import ConfigManager
from src.Bank_term_deposit_sub_pred.components.Data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass 

    def main(self):
        config=ConfigManager()
        data_transformation_config=config.get_data_tranformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.preprocessing_data()
