import os
import sys 
import logging

# define logging format
log_str="[%(asctime)s : %(levelname)s : %(module)s :%(message)s]"

# get current directory path
curr_dir=os.path.abspath(os.path.dirname(__file__))

#define log folder and log filepath
log_dir=os.path.join(curr_dir,"logs")
log_path=os.path.join(log_dir,"running_logs.log")

# create log directory if doesn't exists
os.makedirs(log_dir,exist_ok=True)

# configure logging to write logs for both file and console
logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

# create logger object for project
logger=logging.getLogger("bank_term_deposite_sub_prediction")



