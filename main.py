from src.Bank_term_deposit_sub_pred.logging import logger
from src.Bank_term_deposit_sub_pred.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Bank_term_deposit_sub_pred.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Bank_term_deposit_sub_pred.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.Bank_term_deposit_sub_pred.pipeline.stage_04_model_trainer import ModelTrainerPipepline
from src.Bank_term_deposit_sub_pred.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


# data ingestion stage variable
stage_one="Data Ingestion"

# data ingestion pipeline
if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_one} completed >>>>\n")
    except Exception as e:
        logger.info(e)
        raise e

stage_two="Data Validation"

# data validation pipeline
if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_two} started >>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_two} completed >>>>\n")
    except Exception as e:
        logger.info(e)
        raise e

stage_three="Data Transformation"

# data Transformation pipeline
if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_three} started >>>>")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_three} completed >>>>\n")
    except Exception as e:
        logger.info(e)
        raise e
    
stage_four="Model Trainer"

# model trainer pipeline
if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_four} started >>>>")
        obj=ModelTrainerPipepline()
        obj.main()
        logger.info(f"<<<< stage: {stage_four} completed >>>>\n")
    except Exception as e:
        logger.info(e)
        raise e


stage_five="Model evaluation"
# model evaluation pipeline
if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_five} started >>>>")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_five} completed >>>>\n")
    except Exception as e:
        logger.info(e)
        raise e
        
        
        