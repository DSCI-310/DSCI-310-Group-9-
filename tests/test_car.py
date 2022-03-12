import pandas as pd
import sys
sys.path.append( '/DSCI-310-Group-9-' )
from src.features import features

car_table = pd.read_csv('data/car.data', sep = ",", header=None, names = ["price", "maint", "doors", "persons", "lug_boot", "safety", "class"],)


def test_features():
    expected = car_table.shape[1] - 1
    actual = features(car_table, 'price')
    assert actual == expected, 'Number of columns are not equal!'