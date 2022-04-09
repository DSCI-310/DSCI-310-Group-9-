import pandas as pd
from pandas import DataFrame


def rm_null(df: DataFrame):
    """
    Remove null values

    Checks if the inputted dataframe has any null values, and removes them if they exist, otherwise
    will return the unchanged dataframe
    :param df: a dataframe or dataframe extension
    :return: a dataframe

    example:
    rm_null(car_table)
    """
    if not df == pd.DataFrame():
        raise TypeError("Input must be a DataFrame")
        
    if df.isnull().values.any():
        return df.dropna()
    else:
        return df
