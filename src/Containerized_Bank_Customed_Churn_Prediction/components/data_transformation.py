import os 
from src.Containerized_Bank_Customed_Churn_Prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from src.Containerized_Bank_Customed_Churn_Prediction.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        

    def prep_for_pipeline(self):
        data = pd.read_csv(self.config.data_path)

        df = data.copy()
        
        y = df['churn']

        df.drop(columns=['churn','customer_id'],inplace=True)

        X = df

        num_cols = X.select_dtypes(include=['int64','float64']).columns
        cat_cols = X.select_dtypes(include=['object']).columns

        return X,num_cols,cat_cols,y


    def num_cat_pipelines(self,num_cols,cat_cols):

        num_pipe = Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='mean')),
            ('StandardScaler',StandardScaler())
        ])
        
        cat_pipe = Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('one-hot',OneHotEncoder(handle_unknown='ignore'))
        ])

        preprocessor=ColumnTransformer(
            transformers=[
                ('num',num_pipe,num_cols),
                ('cat',cat_pipe,cat_cols)
            ]
        )

        return preprocessor


    def full_pipeline(self,preprocessor,model):
        parameters=self.config.parameters

        full_pipe =Pipeline(steps=[
                ('preprocessor',preprocessor),
                ('model', model(**parameters))
            ])

        return full_pipe

    def train_test_split(self,X,y):
            
            X_train, X_test, y_train, y_test = train_test_split(
                 X, y, test_size=0.2, random_state=42, stratify=y
                )

            train = pd.concat([X_train, y_train], axis=1)
            test = pd.concat([X_test, y_test], axis=1)
       
            train.to_csv(os.path.join(self.config.root_dir,'train.csv'), index = False)
            test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

            logger.info(f"Split işlemi yapıldı")
            print(train.shape)
            print(test.shape)