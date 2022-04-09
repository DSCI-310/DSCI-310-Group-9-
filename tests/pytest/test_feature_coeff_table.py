from ctypes import c_uint16
import pandas as pd
import numpy as np
import sys

from src.feature_coeff_table import build_coef_dataframe

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

