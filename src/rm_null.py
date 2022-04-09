import pandas as pd
from pandas import DataFrame

# rm_null
#
# A function which Checks if the inputted dataframe has any null values, 
# and removes them if they exist, otherwise will return the unchanged dataframe
#
# @param df A data frame which contains 2 columns, one for class names, and one for their corresponding values
#
# @return
#
# @export
#
# @example
# rm_null(mydf)
def rm_null(df: DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")

    if df.isnull().values.any():
        return df.dropna()
    else:
        return df
