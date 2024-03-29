import logging
import os
from datetime import datetime

#log filename
LOG_FILE_NAME=f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#log filedir

LOG_FILE_DIR=os.path.join(os.getcwd(),"logs")

#createfile if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
Log_FILE_PATH=os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
  filename=Log_FILE_PATH,
  format="[ %(asctime)s ]%(lineno)d%(name)s - %(levelname)s - %(message)s",
  level=logging.INFO,

)