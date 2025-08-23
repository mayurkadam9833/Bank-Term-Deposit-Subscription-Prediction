import os
import yaml
import json
from pathlib import Path 
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations 
from src.Bank_term_deposit_sub_pred.logging import logger


# function to read yaml file 
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml,"r")as yaml_file:
            content=yaml.safe_load(path_to_yaml)
            logger.info(f"yaml file loaded sucuessfully from {path_to_yaml}")
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e 

# function to create a new directory
def create_dir(file_path=list,verbose=True):
    for path in file_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"{path} create scuessfully")

# fuction to get size of file 
def get_size(file):
    size_in_kb=round(os.path.getsize(file))
    return f"File size : {size_in_kb} KB"

# function to create and save a json file 
def save_json(path:Path,data:dict):
    with open(path,"w")as file:
        json.dump(data,file)
        logger.info(f"json file save sucessfully at : {path}")

