from car_analysis import *
import pandas as pd
import numpy as np
from pandas import DataFrame
from ctypes import c_uint16
import pandas as pd
import sys
import pytest
sys.path.append( '/DSCI-310-Group-9-')
import matplotlib.figure

@pytest.fixture
def not_a_dataframe():
    return 10

@pytest.fixture
def not_a_string():
    return 10


@pytest.fixture
def normal_dataframe():
    data = {"features": ["vanilla", "chocolate"], "coefficients": [-0.1, 0.6]}
    return pd.DataFrame(data)

@pytest.fixture
def bad_dataframe():
    data = {"features": ["vanilla", "chocolate"], "coefficients": ["ice cream", 0.6]}
    return pd.DataFrame(data)
  
@pytest.fixture
def na_dataframe():
    data = {"features": ["vanilla", "chocolate"], "coefficients": [None, 0.6]}
    return pd.DataFrame(data)
  
@pytest.fixture
def only_na_dataframe():
    data = {"features": ["vanilla", "chocolate"], "coefficients": [None, None]}
    return pd.DataFrame(data)

@pytest.fixture
def normal_x_name():
    return "features"


@pytest.fixture
def normal_y_name():
    return "coefficients"

# tests for rm_null  
def test_not_a_df():
    expected = TypeError
    actual = rm_null(not_a_dataframe)
    assert isinstance(actual, expected)
    
def test_df_no_na():
    expected = normal_dataframe
    actual = rm_null(normal_dataframe)
    assert actual.equals(expected)
    
def test_df_with_na(na_dataframe):
    na = na_dataframe
    expected = na.dropna()
    actual = rm_null(na_dataframe)
    assert actual.equals(expected)
    
def test_df_only_na(only_na_dataframe):
    all_na = only_na_dataframe
    expected = all_na.dropna()
    actual = rm_null(only_na_dataframe())
    assert actual.equals(expected)


# tests for features

# testing features function
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


# tests for build_coef_dataframe
features = ["feature1", "featuren2", "feature3"]
coeffs = np.array([1, 2, 3])

def test_correct_input():
    expected = pd.DataFrame({"features":features, "coefficient":coeffs})
    actual = build_coef_dataframe(features, coeffs)
    assert actual.equals(expected), 'Works when the input are correctly formatted'

def test_incorrect_features_type():
    expected = RuntimeError
    actual = build_coef_dataframe("feature123", coeffs)

def test_incorrect_feature_type():
    expected = RuntimeError
    actual = build_coef_dataframe(["feature1", 2, "feature3"], coeffs)

def test_incorrect_coeffs_type():
    expected = RuntimeError
    actual = build_coef_dataframe(features, [1, 2, 3])


# tests for visualize_coefficients
# Tests that normal inputs will result in a pandas figure
def test_normal_dataframe(normal_dataframe, normal_x_name, normal_y_name):
    expected = matplotlib.figure.Figure
    figure = visualize_coefficients(normal_dataframe, "mygraph", normal_x_name, normal_y_name)
    actual = type(figure)
    assert actual == expected

# Tests that not passing a dataframe will result in an AttributeError
def test_not_a_dataframe(not_a_dataframe, normal_x_name, normal_y_name):
    expected = AttributeError
    actual = visualize_coefficients(not_a_dataframe, "mygraph", normal_x_name, normal_y_name)
    assert isinstance(actual, expected)

# Tests that not passing in a string for x_name will result in a RuntimeError
def test_invalid_x_name(normal_dataframe, not_a_string, normal_y_name):
    expected = RuntimeError
    actual = visualize_coefficients(normal_dataframe, "mygraph", not_a_string, normal_y_name)
    assert isinstance(actual, expected)

# Tests that not passing in a string for y_name will result in a RuntimeError
def test_invalid_y_name(normal_dataframe, normal_x_name, not_a_string):
    expected = RuntimeError
    actual = visualize_coefficients(normal_dataframe, "mygraph", normal_x_name, not_a_string)
    assert isinstance(actual, expected)

# Tests that non number values in the y_name column will result in a TypeError
def test_bad_dataframe(bad_dataframe, normal_x_name, normal_y_name):
    expected = TypeError
    actual = visualize_coefficients(bad_dataframe, "mygraph", normal_x_name, normal_y_name)
    assert isinstance(actual, expected)
