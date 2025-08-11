import os 
from src.Containerized_Bank_Customed_Churn_Prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.Containerized_Bank_Customed_Churn_Prediction.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
        
    def train(self):

        preprocessor = joblib.load("artifacts/data_transformation/preprocessor.pkl")
        
        parameters=self.config.parameters
        model_class = RandomForestClassifier

        full_pipe =Pipeline(steps=[
                ('preprocessor',preprocessor),
                ('model', model_class(**parameters))
            ])



        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop(self.config.target_column,axis = 1)
        test_x = test_data.drop(self.config.target_column,axis = 1)

        train_y = train_data[[self.config.target_column]]
        test_y =  test_data[[self.config.target_column]]


        full_pipe.fit(train_x, train_y.values.ravel())

        joblib.dump(full_pipe, os.path.join(self.config.root_dir,self.config.model))