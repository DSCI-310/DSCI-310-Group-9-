import pytest
import pandas as pd



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
