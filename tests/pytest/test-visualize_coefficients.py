import pytest
import sys
import pandas as pd

sys.path.append('/DSCI-310-Group-9-')
from src.visualize_coefficients import visualize_coefficients

@pytest.fixture
def not_a_dataframe():
    return 10

@pytest.fixture
def not_a_string():
    return 10

@pytest.fixture
def normal_dataframe():
    data = {"features": ["vanilla", "chocolate"], "coefficients": [-0.1, 0.6]}
    return pd.dataframe(data)

@pytest.fixture
def normal_x_name():
    return "features"

@pytest.fixture
def normal_y_name():
    return "coefficients"
