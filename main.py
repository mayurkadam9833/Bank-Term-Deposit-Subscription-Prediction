from src.Bank_term_deposit_sub_pred.logging import logger
from src.Bank_term_deposit_sub_pred.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Bank_term_deposit_sub_pred.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Bank_term_deposit_sub_pred.pipeline.stage_03_data_transformation import DataTransformationPipeline
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
        
        