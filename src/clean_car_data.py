import sys, os

sys.path.append(os.path.join(os.getcwd(), "lib"))
import argparse
import pandas as pd
from rm_null import rm_null

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="file_path", type=str)
parser.add_argument("out_file_path", help="out_file_path")
args = parser.parse_args()

car_table = pd.read_csv(args.file_path, sep=",", header=None,
                        names=["price", "maint", "doors", "persons", "lug_boot", "safety", "class"], )
rm_null(car_table)

car_table.to_csv(args.out_file_path, index = False, header=False)
