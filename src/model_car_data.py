import sys, os

sys.path.append(os.path.join(os.getcwd(), "lib"))
import argparse
import pandas as pd
#from pandas.table.plotting import tablebelow
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


from features import features
from visualize_coefficients import visualize_coefficients
from feature_coeff_table import feature_coef_table

parser = argparse.ArgumentParser()
parser.add_argument("processed_csv_path", help="processed_csv_path")
parser.add_argument("coefficient_graph_path", help="coefficient_graph_path")
parser.add_argument("cross_validation_path", help="cross_validation_path")
parser.add_argument("feature_coefficients_path", help="feature_coefficients_path")
parser.parse_args()
#parser.add_argument("results_figure_path", help="results_figure_path")
args = parser.parse_args()

car_table = pd.read_csv(args.processed_csv_path, sep=",", header=[0])

# splitting of target variable and features
X_car = features(car_table, 'price')
Y_car = car_table['price']


# splitting of data frame into training and testing data
X_train, X_Test, y_train, y_test = train_test_split(X_car, Y_car, test_size=0.2, random_state=1)

feats = ["maint", "doors", "persons", "lug_boot", "safety", "class"]


# fitting model for classification analysis

lr = LogisticRegression(max_iter=1000, C=100)
lr.fit(X_train, y_train)

coeffs = lr.coef_[3]

score = cross_validate(lr, X_Test, y_test, cv=10)


#visualizations
score_df = pd.DataFrame(score)
fig, ax = plt.subplots()
ax.axis("off")
ax.axis("tight")
ax.table(cellText=score_df.values, colLabels=score_df.columns, loc="center")
fig.savefig(args.cross_validation_path)

fig, ax = plt.subplots()
ax.axis("off")
ax.axis("tight")
df1 = feature_coef_table(feats, coeffs)
ax.table(cellText=df1.values, colLabels=df1.columns, loc="center")
fig.savefig(args.feature_coefficients_path)


fig = visualize_coefficients(df1, "Graph of training coefficients", "features", "coefficient")
fig.savefig(args.coefficient_graph_path)