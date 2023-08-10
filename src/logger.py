import logging    
import os 
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #fstring is used ,the logs will be in this format 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#logs will be created in the current directory 
os.makedirs(logs_path,exist_ok=True)#keepon appending the file 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)