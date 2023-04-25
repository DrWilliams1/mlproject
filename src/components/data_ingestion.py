import os 
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


"""defining a function inside a function"""
@dataclass

#This class is requiring any input component
class DataIngestionConfig:
   
    """(Path )for data ingestion component and all of the files will
    be saved in the artifacts folder"""
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    raw_data_path: str=os.path.join("artifacts", "data.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig
        """This will consist of the (3 variables) being saved
        inside the dataingestionconfig"""

   
   
    """Reading the dataset"""
    def initiate_data_ingestion(self):
        logging.info('Entered the Data ingestion method or component')
        try:
            """Can read from anywhere but (reading from the csv) in this instance"""
            df=pd.read_csv('C:\Projects\mlproject\mlproject-1\notebook\data')
            logging.info('Read the dataset as dataframe')
            """Continue to write log so when an exception happen I can know where"""

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            """Getting directory name in respect to a specific path> If its already there
             we will keep it. """
            
            """Saving the data path also to csv file"""
            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            logging.info('Train Test Split initiated')
            train_set, test_set=train_test_split(df, test_size=0.2, random_state=42)

            """Saving to the path"""
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of the data is completed')

            """Returning the data paths"""
            return(
                self.ingestion_config.test_data_path, 
                self.ingestion_config.test_data_path
                
            )
        
        except Exception as e:
            raise CustomException(e, sys)


   
if __name__=="main":
    obj=DataIngestion()
    obj.iniate_data_ingestion()

