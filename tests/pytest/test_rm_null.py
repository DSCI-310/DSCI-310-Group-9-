import pandas as pd
from pandas import DataFrame
from ctypes import c_uint16
import pandas as pd
import sys
sys.path.append( '/DSCI-310-Group-9-' )
from src.rm_null import rm_null
from helper_visualize_coefficients import *
  
  
def test_not_a_df():
    expected = TypeError
    actual = rm_null(not_a_dataframe)
    assert isinstance(actual, expected)
    
def test_df_no_na():
    expected = normal_dataframe
    actual = rm_null(normal_dataframe)
    assert actual.equals(expected)
    
def test_df_with_na():
    expected = na_dataframe.dropna()
    actual = rm_null(na_dataframe)
    assert actual.equals(expected)
