from src.Containerized_Bank_Customed_Churn_Prediction.config.configuration import ConfigurationManager
from src.Containerized_Bank_Customed_Churn_Prediction.components.data_transformation import DataTransformation
from src.Containerized_Bank_Customed_Churn_Prediction import logger
from sklearn.ensemble import RandomForestClassifier

STAGE_NAME= ' >>>>>>>DATA TRANSFORMATİON <<<<< '


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        X, num_cols, cat_cols, y = data_transformation.prep_for_pipeline()
        preprocessor=data_transformation.num_cat_pipelines(num_cols,cat_cols)
        full_pipeline=data_transformation.full_pipeline(preprocessor,model=RandomForestClassifier)
        data_transformation.train_test_split(X,y)


if __name__ == '__main__':
   try:
    logger.info(f"{STAGE_NAME}")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} BİTTİ")

   except Exception as e:
    logger.info(e)
    raise e