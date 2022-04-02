import sys, os

sys.path.append(os.path.join(os.getcwd(), "lib"))
import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="file_path", type=str)
parser.add_argument("out_file_path", help="out_file_path")
args = parser.parse_args()

car_table = pd.read_csv(args.file_path, sep=",", header=None,
                        names=["price", "maint", "doors", "persons", "lug_boot", "safety", "class"], )

price = pd.DataFrame(car_table["price"])


plt.hist(price, bins=7)
plt.xlabel("Price")
plt.ylabel("Count")
plt.title("Figure 1: Distribution of Price Variable")
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.savefig(args.out_file_path)