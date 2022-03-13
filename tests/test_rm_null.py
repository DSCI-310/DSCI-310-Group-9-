import pandas as pd
from pandas import DataFrame
from ctypes import c_uint16
import pandas as pd
import sys
sys.path.append( '/DSCI-310-Group-9-' )
from src.rm_null import rm_null

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
