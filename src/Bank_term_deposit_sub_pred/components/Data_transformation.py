import os 
import pandas as pd 
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from src.Bank_term_deposit_sub_pred.entity.config_entity import DataTransformationConfig

"""
class for data transformation contained methods 
-> preprocess data
will return preprocessed data with train test split
"""

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config 
        self.encode=LabelEncoder()
        self.scale=StandardScaler()
        self.sampling=SMOTE()
    
    # method to preprocess data including encode,scale,and train test split
    def preprocessing_data(self):
            try:
                # read data from defined path
                data=pd.read_csv(self.config.data_path,sep=";")
                #encode categorical data
                data[data.select_dtypes(include=["object"]).columns]=data[data.select_dtypes(include=["object"]).columns].apply(self.encode.fit_transform)
                # save encoder as model
                joblib.dump(self.encode,os.path.join(self.config.root_dir,"encode.joblib"))

                #split data input and target column
                input_data=data.drop([self.config.target_col],axis=1)
                target_col=data[self.config.target_col]

                # train and split data
                train_x,test_x,train_y,test_y=train_test_split(input_data,target_col,test_size=0.2,random_state=42)

                # perform oversampling for imbalanced data
                sample_train_x,sampled_train_y=self.sampling.fit_resample(train_x,train_y)

                # features scaling on input data
                scale_train_x=self.scale.fit_transform(sample_train_x)
                scale_test_x=self.scale.transform(test_x)

                # save scaling as model
                joblib.dump(self.scale,os.path.join(self.config.root_dir,"scale.joblib"))

                # contcat train_x and train_y return train_data
                train_data=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),pd.DataFrame(sampled_train_y).reset_index(drop=True)],axis=1)
                # contcat test_x and test_y return train_data
                test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),pd.DataFrame(test_y).reset_index(drop=True)],axis=1)

                # save csv files to data transformation folder
                train_data.to_csv(os.path.join(self.config.root_dir,"Train_data.csv"))
                test_data.to_csv(os.path.join(self.config.root_dir,"Test_data.csv"))

            except Exception as e:
                raise e


    




