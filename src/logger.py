import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs", LOG_FILE)
"""Whatever logs get created it will be within the current working directory"""
os.makedirs(logs_path,exist_ok=True)
"""This just says keeping appending files whenever created"""


LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,

)

