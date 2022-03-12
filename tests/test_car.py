from ctypes import c_uint16
import pandas as pd
import sys
sys.path.append( '/DSCI-310-Group-9-' )
from src.features import features

car_table = pd.read_csv('data/car.data', sep = ",", header=None, names = ["price", "maint", "doors", "persons", "lug_boot", "safety", "class"],)

features(1, '1')

# testing features function
def test_same_columnSize():
    expected = car_table.shape[1] - 1
    actual = features(car_table, 'price').shape[1]
    assert actual == expected, 'Number of columns are not equal!'

def test_same_rowSize():
    expected = car_table.shape[0]
    actual = features(car_table, 'price').shape[0]
    assert actual == expected, 'Number of rows are not equal!'

def test_same_value():
    expected = car_table['maint'][0]
    actual = features(car_table, 'price')['maint'][0]
    assert actual == expected, 'First value is not the same'