from src.Containerized_Bank_Customed_Churn_Prediction import logger 
from src.Containerized_Bank_Customed_Churn_Prediction.pipeline.ingestion_01 import DataIngestionTrainingPipeline
from src.Containerized_Bank_Customed_Churn_Prediction.pipeline.validation_02 import DataValidationTraininPipeline
from src.Containerized_Bank_Customed_Churn_Prediction.pipeline.transformation_03 import DataTransformationTrainingPipeline
from src.Containerized_Bank_Customed_Churn_Prediction.pipeline.m_trainer_04 import ModelTrainerTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} başladı <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" {STAGE_NAME} aşaması tamamlandı")


except Exception as e:
    raise e



STAGE_NAME = ">>>>>>>>>>DATA VALİDATİON STAGE <<<<<<<<<<<"

try:
   logger.info(f"{STAGE_NAME} BAŞLADI")
   data_validation =DataValidationTraininPipeline()
   data_validation.main()
   logger.info(f"{STAGE_NAME} BİTTİ!!")
   
except Exception as e:
   logger.info(e)
   raise e


STAGE_NAME = ' >>>>>>>DATA TRANSFORMATİON <<<<< '

try:
    logger.info(f"{STAGE_NAME} başladı")
    data_transformation =DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME} bitti")

except Exception as e:
    logger.info(e)
    raise


STAGE_NAME = '>>>>>>MODEL TRAINER<<<<<<<<<'

try:
    logger.info(f"{STAGE_NAME} kısmı başladı")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"{STAGE_NAME} kısmı bitti")

except Exception as e:
    logger.info(e)
    raise