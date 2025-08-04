from src.Containerized_Bank_Customed_Churn_Prediction import logger 
from src.Containerized_Bank_Customed_Churn_Prediction.pipeline.ingestion_01 import DataIngestionTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} başladı <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" {STAGE_NAME} aşaması tamamlandı")


except Exception as e:
    raise e