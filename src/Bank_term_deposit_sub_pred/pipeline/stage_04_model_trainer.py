from src.Bank_term_deposit_sub_pred.config.configuration import ConfigManager
from src.Bank_term_deposit_sub_pred.components.model_trainer import ModelTrainer

"""
This model trainer Pipeline class called function train modelwhich will train model
"""
class ModelTrainerPipepline:
    def __init__(self):
        pass
    
    # model training pipeline
    def main(self):
        config=ConfigManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train_model()

