import sys, os

sys.path.append(os.path.join(os.getcwd(), "lib"))
import argparse
import pandas as pd

from sklearn.model_selection import cross_validate, train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer

parser = argparse.ArgumentParser()
parser.add_argument("cleaned_csv_path", help="cleaned_path", type=str)
parser.add_argument("processed_file_path", help="processed_out_path")
args = parser.parse_args()

# categorizing features(price, maint, doors, persons, lug_boot, safety, class) to be used a in column transformer to enable easy manipulation of data frame
car_table = pd.read_csv(args.cleaned_csv_path, sep=",", header=None,
                        names=["price", "maint", "doors", "persons", "lug_boot", "safety", "class"], )

ordinal_feats = ["price", "maint", "doors", "persons", "lug_boot", "safety", "class"]

# categories of each feature
maint_levels = ['low', 'med', 'high', 'vhigh']
doors_levels = ['2', '3', '4', '5more']
persons_levels = ['2', '4', 'more']
boot_levels = ['small', 'med', 'big']
safety_levels = ['low', 'med', 'high']
class_levels = ['unacc', 'acc', 'good', 'vgood']

# ordinal encoding of each feature
column_transformer = make_column_transformer(
    (OrdinalEncoder(
        categories=[maint_levels, maint_levels, doors_levels, persons_levels, boot_levels, safety_levels, class_levels],
        dtype=int),
     ordinal_feats)
)

X_transformed = column_transformer.fit_transform(car_table)
column_names = ordinal_feats

# creating new table after data preprcoessing
new_table = pd.DataFrame(X_transformed, columns=column_names)
print(new_table)

new_table.to_csv(args.processed_file_path, index=False)

