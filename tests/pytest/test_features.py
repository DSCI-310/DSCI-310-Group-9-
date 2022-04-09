from ctypes import c_uint16
import pandas as pd
import sys
import numpy as np
import pytest
sys.path.append( '/DSCI-310-Group-9-' )
from src.features import features

car_table = pd.read_csv('data/car.data', sep = ",", header=None, names = ["price", "maint", "doors", "persons", "lug_boot", "safety", "class"],)



# testing features function
def test_same_columnSize():
    expected = car_table.shape[1] - 1
    actual = features(car_table, 'price').shape[1]
    assert actual == expected, 'Number of columns are not equal!'


# testing rows are equal
def test_same_rowSize():
    expected = car_table.shape[0]
    actual = features(car_table, 'price').shape[0]
    assert actual == expected, 'Number of rows are not equal!'

# testing if column stays the same
def test_same_value():
    expected = car_table['maint'][0]
    actual = features(car_table, 'price')['maint'][0]
    assert actual == expected, 'First value is not the same'

# right input
def test_right_input1():
    #expected
    df2 = pd.DataFrame(np.array([[1, 2], [4, 5], [7, 8,]]),
                   columns=['a', 'b'])

    # random data frame
    df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

    expected = df2
    actual = features(df1, 'c')
    assert expected.equals(actual)


def test_right_input2():
    df1 = pd.DataFrame(np.array([['a', 'b','c'], ['a', 'b','c']]),
                   columns=['a', 'b', 'c'])
    
    df2 = pd.DataFrame(np.array([['b','c'], ['b','c']]),
                   columns=['b', 'c'])
    actual = features(df1, 'a')
    expected = df2

    assert expected.equals(actual)


def test_wrong_input():
    df1 = pd.DataFrame(np.array([['a', 'b','c'], ['a', 'b','c']]),
                   columns=['a', 'b', 'c'])
    
    with pytest.raises(AssertionError):
        assert df1.equals(features(df1, df1))
