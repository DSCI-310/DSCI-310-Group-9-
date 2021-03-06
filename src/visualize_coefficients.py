import pandas as pd
import matplotlib.pyplot as plt

# visualize_coefficients
#
# A function which creates a bar graph given a dataframe of classes and their values.
#
# @param df A data frame which contains 2 columns, one for class names, and one for their corresponding values
# @param title string of Title of the graph
# @param x_name string of the Name of the column of classes
# @param y_name string of the Name of the column of values
#
# @return
#
# @export
#
# @example
# visualize_coefficients(mydf, "mygraph", "x-axis", "y-axis")
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
