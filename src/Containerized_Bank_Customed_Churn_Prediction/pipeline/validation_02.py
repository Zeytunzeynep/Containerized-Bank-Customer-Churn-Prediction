from src.Containerized_Bank_Customed_Churn_Prediction.config.configuration import ConfigurationManager
from src.Containerized_Bank_Customed_Churn_Prediction.components.data_validation import DataValidation
from src.Containerized_Bank_Customed_Churn_Prediction import logger



STAGE_NAME = ">>>>>>>>>>DATA VALİDATİON STAGE <<<<<<<<<<<"

class DataValidationTraininPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__' :
 try:
    logger.info(f"{STAGE_NAME}")
    obj = DataValidationTraininPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} BİTTİ")

 except Exception as e:
    logger.info(e)
    raise e