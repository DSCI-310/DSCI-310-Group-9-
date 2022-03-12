import matplotlib.figure
from src.visualize_coefficients import visualize_coefficients
from helper_visualize_coefficients import *

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