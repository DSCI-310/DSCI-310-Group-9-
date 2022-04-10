import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest
from pandas import DataFrame

#' rm_null
#'
#' A function which Checks if the inputted dataframe has any null values, 
#' and removes them if they exist, otherwise will return the unchanged dataframe
#'
#' @param df A data frame which contains 2 columns, one for class names, and one for their corresponding values
#'
#' @return
#'
#' @export
#'
#' @example
#' rm_null(mydf)

def rm_null(df: DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")

    if df.isnull().values.any():
        return df.dropna()
    else:
        return df


#' features
#'
#' Dataframe of dependent variables
#'
#' Creates a new data frame without the given targetValue
#'
#' @param data_frame A data frame or data frame extension (e.g. a tibble).
#' @param target_Value as String, column containing the dependent variable
#'
#' @return A data frame with the given target_Value. 
#'   Each column (excluding target_Value) lists the possible inputs for the given feature.
#'
#' @examples features(car_table, price)

def features(data_frame, target_Value):
    return data_frame.drop(columns=target_Value)

# return a data frame without one column: targetValue

#' build_coef_dataframe
#'
#' Dataframe of features and their coefficients
#'
#' Build a dataframe containing features and their coefficients
#'
#' @param feats A list of String representing the features.
#' @param coeffs A numpy array of double representing the coefficients of the features
#'
#' @return A data frame containing features and their coefficients
#'
#' @examples features(feats, coeffs)
def build_coef_dataframe(feats, coeffs):

    try:
        if (not isinstance(feats, list)):
            raise RuntimeError("expect a list for features.")
        if (not isinstance(coeffs, np.ndarray)):
            raise RuntimeError("expect a list for features.")
        for i in f:
            if (not isinstance(i, str)):
                raise RuntimeError("all features should have type String.")
        
        data = {"features":feats, "coefficient":coeffs}
        df1 = pd.DataFrame(data)
        df1 = df1.sort_values(by=['coefficient'])
        return df1
    except RuntimeError as err:
        print(str(err))


#' visualize_coefficients
#'
#' A function which creates a bar graph given a dataframe of classes and their values.
#'
#' @param df A data frame which contains 2 columns, one for class names, and one for their corresponding values
#' @param title string of Title of the graph
#' @param x_name string of the Name of the column of classes
#' @param y_name string of the Name of the column of values
#'
#' @return
#'
#' @export
#'
#' @example
#' visualize_coefficients(mydf, "mygraph", "x-axis", "y-axis")

def visualize_coefficients(df, title, x_name, y_name):

    colors = {'Negative' : 'red', 'Positive' : 'blue'}
    labels = colors.keys()
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    
    try:
        if not isinstance(x_name, str) or not isinstance(y_name,str):
            raise RuntimeError("Not a string")
        if not isinstance(df, pd.DataFrame):
            raise AttributeError("Not a DataFrame")
    except Exception as err:
        return err

    try:
        df = df.sort_values(by=y_name)
    except TypeError as err:
        return err

    fig2 = plt.figure()

    axes = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.set_title(title)
    axes.set_xlabel(x_name)
    axes.set_ylabel(y_name)

    for index, row in df.iterrows():
        if row[y_name] < 0:
            axes.bar(row[x_name], row[y_name], color="red", label="Negative Values")
        else:
            axes.bar(row[x_name], row[y_name], color="blue")

    axes.legend(handles, labels, loc="upper left")

    return fig2
