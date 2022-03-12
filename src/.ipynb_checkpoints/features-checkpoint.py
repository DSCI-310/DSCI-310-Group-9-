import pandas as pd
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
    try:
        if(not isinstance(target_Value, str)):
            raise RuntimeError("Not a string")
        if(not isinstance(data_frame, pd.DataFrame)):
            raise RuntimeError("Not a dataframe")
        
        return data_frame.drop(columns=target_Value)
    except AttributeError as err:
        print("Not a dataframe, data_frame", err)
    except RuntimeError:
        print("Not a string/data frame")
        
    # return a data frame without one column: targetValue