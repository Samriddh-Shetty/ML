import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataInjectionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataInjection:
    def __init__(self):
        self.DataInjection_config=DataInjectionConfig()
    
    def initiate_data_injection(self):
        logging.info("Enter the data Injection Method")

        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as DataFrame")

            os.makedirs(os.path.dirname(self.DataInjection_config.train_data_path),exist_ok=True)

            df.to_csv(self.DataInjection_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.20,random_state=42)

            train_set.to_csv(self.DataInjection_config.train_data_path,index=False,header=False)

            test_set.to_csv(self.DataInjection_config.test_data_path,index=False,header=False)

            logging.info("Injection of data is completed")

            return( self.DataInjection_config.train_data_path,
                   self.DataInjection_config.test_data_path,
                   
                   )
    

        except  Exception as e:
            raise CustomException(e,sys)  




if __name__== "__main__":
    obj = DataInjection()
    obj.initiate_data_injection()       
