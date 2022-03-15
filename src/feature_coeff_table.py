import pandas as pd
import numpy as np

#' Dataframe of features and their coefficients
#'
#' Build a dataframe containing features and their coefficients
#'
#' @param f A list of String representing the features.
#' @param c A numpy array of double representing the coefficients of the features
#'
#' @return A data frame containing features and their coefficients
#'
#' @examples features(feats, coeffs)
def feature_coef_table(f, c):

    try:
        if (not isinstance(f, list)):
            raise RuntimeError("expect a list for features.")
        if (not isinstance(c, np.ndarray)):
            raise RuntimeError("expect a list for features.")
        for i in f:
            if (not isinstance(i, str)):
                raise RuntimeError("all features should have type String.")
        
        data = {"features":f, "coefficient":c}
        df1 = pd.DataFrame(data)
        df1 = df1.sort_values(by=['coefficient'])
        return df1
    except RuntimeError as err:
        print(str(err))