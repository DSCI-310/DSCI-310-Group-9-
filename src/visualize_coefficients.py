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
    df = df.sort_values(by=y_name)

    fig2 = plt.figure()
    axes = fig2.add_axes([0, 0, 1, 1])
    axes.set_title(title)
    axes.set_xlabel(x_name)
    axes.set_ylabel(y_name)

    for index, row in df.iterrows():
        print(row)

    # axes.bar(df['features'][:2], df['coefficient'][:2], color="red")
    # axes.bar(df['features'][2:], df['coefficient'][2:])
    # plt.show()
