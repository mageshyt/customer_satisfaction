import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataPreProcessStrategy,DataCleaninig,DataSplitStrategy

from typing import Annotated, Tuple

@step
def clean_data(data: pd.DataFrame) -> Tuple[
             Annotated[pd.DataFrame, 'X_train'],
          Annotated[pd.DataFrame, 'X_test'],
          Annotated[pd.DataFrame, 'y_train'],
          Annotated[pd.DataFrame, 'y_test']]:
    """
    Cleaning the data.

    Args:
        data (pd.DataFrame): data to be cleaned

    Returns:
         Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]: cleaned data
    """
    try:
        logging.info("Cleaning data")
        # Data cleaning
        process_strategy = DataPreProcessStrategy(data)
        data_cleaning=DataCleaninig(data,process_strategy)
        processed_data= data_cleaning.handle_data()
        # Splitting the data
        split_strategy=DataSplitStrategy(processed_data)

        X_train ,X_test,y_train,y_test=split_strategy.handle_data()

        logging.info("Data cleaning complete !")

        return X_train ,X_test,y_train,y_test
    
    except Exception as e:
        logging.error(f"An error occurred while cleaning the data: {e}")
        raise e