import pandas as pd
from pandas import DataFrame


def rm_null(df: DataFrame):
    """
    Remove null values

    Checks if the inputted dataframe has any null values, and removes them if they exist, otherwise
    will print that no null values are present
    :param df: a dataframe or dataframe extension
    :return: a dataframe

    example:
    rm_null(car_table)
    """
    if df.isnull().values.any():
        return df.dropna()
    else:
        return df
    
    
def test_rm_null():
    """
    Test remove null values
    """
    na_test = pd.DataFrame({"price": ["low", "med", "high"],
                            "maint": [None, "vhigh", "low"]})
    no_na_test = pd.DataFrame({"price": ["low", "med", "high"],
                               "maint": ["med", "vhigh", "low"]})
    na_expected = na_test.dropna()
    no_na_expected = no_na_test

    na_actual = rm_null(na_test)
    no_na_actual = rm_null(no_na_test)
    assert na_actual.equals(na_expected)
    assert no_na_actual.equals(no_na_actual)