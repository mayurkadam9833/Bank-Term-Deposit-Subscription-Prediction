import os 
import joblib
import pandas as pd 
import numpy as np
from pathlib import Path
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,roc_auc_score
from src.Bank_term_deposit_sub_pred.entity.config_entity import ModelEvaluationConfig
from src.Bank_term_deposit_sub_pred.utils.common import save_json



"""
class for data validation contained methods 
-> Model Evaluation
"""
class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config 
        self.model=joblib.load(self.config.model_path)

    # method to get metrics 
    def get_metrics(self,actual,predicted):
        acc=accuracy_score(actual,predicted)
        cf=confusion_matrix(actual,predicted)
        pr=precision_score(actual,predicted)
        rc=recall_score(actual,predicted)
        f1=f1_score(actual,predicted)
        roc=roc_auc_score(actual,predicted)
        return acc,cf,pr,rc,f1,roc

    # method for model evaluation
    def evaluation(self):
        try:
            data=pd.read_csv(self.config.test_data_path)  # read test data file

            test_x=data.drop([self.config.target_col],axis=1)  # dropping target feature
            test_y=data[self.config.target_col]                # target feature

            test_pred=self.model.predict(test_x)               # prediction for test data

            # get metrics
            test_acc,test_cf,test_pr,test_rc,test_f1,test_roc=self.get_metrics(test_y,test_pred)

            # creating dictionary of metrics
            metrics={"accuracy score:":test_acc,"confusion matrix:":test_cf.tolist(),"precision score:":test_pr,"recall score:":test_rc,"f1 score:":test_f1,"roc auc score:":test_roc}

            # saving metrics file
            save_json(Path("artifacts/model_evaluation/metrics.json"),metrics)
        
        except Exception as e:
            raise e



            
