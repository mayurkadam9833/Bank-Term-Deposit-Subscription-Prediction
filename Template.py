import os
import logging
from pathlib import Path 

#setup logging config for files and directories creation for project 
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

#assign project name
project_name="Bank_term_deposit_sub_pred"

# list of files and file path for project
list_of_files=[
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "schema.yaml", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# create a loop to create a files and path 

for filepath in list_of_files:
    filepath=Path(filepath)
    file_dir,file_name=os.path.split(filepath)  # separate file and filepath

    # create a directories if not exists
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating {file_dir} for {file_name}")
    
    # create files if not exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass 
        logging.info(f"create empty {file_name}")
        
    # if file is alreday exists  
    else:
        logging.info(f"{file_name} is already exists")