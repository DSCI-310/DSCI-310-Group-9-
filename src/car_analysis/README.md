# car_analysis

A package for functions used in car_analysis.ipynb project 

## Installation

```bash
$ pip install car_analysis
```

## Usage

`car_analysis` can be used to process and visualize car data, consisting of four functions: rm_null(), features(), build_coef_dataframe() for processing and visualize_coefficients() for visualizing. It can be used as follows:

```python
from car_analysis import *
file_path = "car_data.csv" # path to your file
data = rm_null(file_path)
feature = features(data, "feature_of_interest")
coefficients = build_coef_dataframe([feature_names], [coefficients])
figure = visualize_coefficients(coefficients, "Title", "x label", "y label")

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`car_analysis` was created by Allan Cho, Fred Zhang, Ayasha Abdalla, Zhe Li. It is licensed under the terms of the MIT license.

## Credits

`car_analysis` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
