from src.Containerized_Bank_Customed_Churn_Prediction.config.configuration import DataValidationConfig
import pandas as pd



class DataValidation:
  
  def __init__(self,config:DataValidationConfig):
    self.config = config

  def validate_all_columns(self) -> bool :
    try:
     validation_status = None
     df = pd.read_csv(self.config.unzip_dir)
     cols = list(df.columns)

     all_schema = self.config.all_schema.keys()

     for col in cols:
       if col not in all_schema:
         validation_status = False
         with open(self.config.status_file,'w') as f:
           f.write(f"{validation_status}")
      
       else:
         validation_status =True
         with open(self.config.status_file,'w') as f:
           f.write(f"{validation_status}")
  

     return validation_status
  
    except Exception as e:
     raise e
