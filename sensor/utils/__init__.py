import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    '''
    Description:This function returns collection as data frame
    ===========================================================
    params:
    database_name:database name
    collection_name:collection_name
    ===========================================================
    return pandas dataframes of collection

    '''
    try:
        logging.info(f"Reading data from database:{database_name} and collection:{collection_name}")
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"found columns:{df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column:_id ")
            df=df.drop("_id",axis=1)
        logging.info(f"Rows and columns")
        return df
    except Exception as e:
        raise SensorException(e,sys)
   