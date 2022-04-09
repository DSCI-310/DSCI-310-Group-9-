from car_analysis import car_analysis
import pandas as pd
from pandas import DataFrame
from ctypes import c_uint16
import pandas as pd
import sys
import pytest
sys.path.append( '/DSCI-310-Group-9-')

# tests for rm_null  
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
    
def test_df_only_na():
    expected = only_na_dataframe.dropna()
    actual = rm_null(only_na_dataframe)
    assert actual.equals(expected)


# tests for features
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


# tests for build_coef_dataframe
features = ["feature1", "featuren2", "feature3"]
coeffs = np.array([1, 2, 3])

def test_correct_input():
    expected = pd.DataFrame({"features":features, "coefficient":coeffs})
    actual = feature_coef_table(features, coeffs)
    assert actual.equals(expected), 'Works when the input are correctly formatted'

def test_incorrect_features_type():
    expected = RuntimeError
    actual = feature_coef_table("feature123", coeffs)

def test_incorrect_feature_type():
    expected = RuntimeError
    actual = feature_coef_table(["feature1", 2, "feature3"], coeffs)

def test_incorrect_coeffs_type():
    expected = RuntimeError
    actual = feature_coef_table(features, [1, 2, 3])


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
