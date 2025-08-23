from src.Bank_term_deposit_sub_pred.logging import logger
from src.Bank_term_deposit_sub_pred.pipeline.stage_01_data_ingestion import DataIngestionPipeline


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
        