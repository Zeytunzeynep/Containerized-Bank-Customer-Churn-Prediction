from src.Containerized_Bank_Customed_Churn_Prediction.config.configuration import ConfigurationManager
from src.Containerized_Bank_Customed_Churn_Prediction.components.data_ingestion import DataIngestion
from src.Containerized_Bank_Customed_Churn_Prediction import logger
from src.Containerized_Bank_Customed_Churn_Prediction.entity.config_entity import DataIngestionConfig

STAGE_NAME = "DATA INGESTION STAGE"


class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):

       config = ConfigurationManager()
       data_ingestion_config = config.get_data_ingestion_config()
       data_ingestion = DataIngestion(config=data_ingestion_config) 
       data_ingestion.download_file()

       if data_ingestion_config.local_data_file is zip:
          data_ingestion.extract_file()

       else:
          print(f" bu dosya zip file değil")


if __name__ == "__main__":
 try:
     logger.info(f" >>>>>>>{STAGE_NAME} başladı<<<<<<<<<<<<")
     obj = DataIngestionTrainingPipeline()
     obj.main()
     logger.info(f">>>>>>>>>>>>>>>{STAGE_NAME} bitti<<<<<<<<<<<")
  
 except Exception as e:
    logger.info(e)
    raise e










