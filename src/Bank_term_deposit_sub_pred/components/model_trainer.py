import os 
import joblib
import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from src.Bank_term_deposit_sub_pred.entity.config_entity import ModelTrainerConfig

"""
class for Model Training contained methods 
-> Train_model
"""
class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
        self.model=AdaBoostClassifier(n_estimators=self.config.n_estimators,learning_rate=self.config.learning_rate)

    # method for train model with parameters 
    def train_model(self):
        try:
            # read train data from train data path
            train_data=pd.read_csv(self.config.train_data_path)

            # split data into input and target column
            train_x=train_data.drop([self.config.target_col],axis=1)
            train_y=train_data[self.config.target_col]
            
            # train model
            self.model.fit(train_x,train_y)

            # save model in model trainer folder
            joblib.dump(self.model,os.path.join(self.config.root_dir,self.config.model_name))
        
        except Exception as e:
            raise e 



            

