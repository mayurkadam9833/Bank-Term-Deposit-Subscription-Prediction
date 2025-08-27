from src.Bank_term_deposit_sub_pred.config.configuration import ConfigManager
from  src.Bank_term_deposit_sub_pred.components.model_evaluation import ModelEvaluation


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluation()