from src.Containerized_Bank_Customed_Churn_Prediction.config.configuration import ConfigurationManager
from src.Containerized_Bank_Customed_Churn_Prediction.components.model_trainer import ModelTrainer
from src.Containerized_Bank_Customed_Churn_Prediction import logger
from src.Containerized_Bank_Customed_Churn_Prediction.entity.config_entity import ModelTrainerConfig

STAGE_NAME = '>>>>>>>>MODEL TRAINER<<<<<<<<<<'


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):

     config = ConfigurationManager()
     model_tariner_config = config.get_model_trainer_config()
     model_trainer = ModelTrainer(config=model_tariner_config)
     model_trainer.train()


if __name__ == '__main__':
   try:
    logger.info(f"{STAGE_NAME} BAŞLADI")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} BİTTİ")

   except Exception as e:
    logger.info(e)
    raise e