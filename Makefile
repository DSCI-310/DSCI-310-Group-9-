#Makefile
#
#
#
# This Makefile runs the analysis and modeling of car data and creates
# tables and plots which visualize the results of the modeling
#
# Usage to run entire analysis: make all
# 		to clean entire analysis: make clean

all: data/csv/cleaned_data.csv data/csv/processed_data.csv data/figures/car_distribution.png data/figures/coefficient_graph.png data/figures/cross_val.png data/figures/feature_coeffs.png doc/car_analysis.html doc/car_analysis.pdf

data/csv/cleaned_data.csv : src/clean_car_data.py data/car.data
	python src/clean_car_data.py data/car.data data/csv/cleaned_data.csv

data/csv/processed_data.csv : src/process_cleaned_car_data.py data/csv/cleaned_data.csv
	python src/process_cleaned_car_data.py data/csv/cleaned_data.csv data/csv/processed_data.csv

data/figures/car_distribution.png : src/visualize_car_data.py data/csv/cleaned_data.csv
	python src/visualize_car_data.py data/csv/cleaned_data.csv data/figures/car_distribution.png

data/figures/coefficient_graph.png data/figures/cross_val.png data/figures/feature_coeffs.png : src/model_car_data.py data/csv/processed_data.csv
	python src/model_car_data.py data/csv/processed_data.csv data/figures/coefficient_graph.png data/figures/cross_val.png data/figures/feature_coeffs.png

# render analysis report to html
doc/car_analysis.html: doc/car_analysis.Rmd doc/references.bib
	Rscript -e "rmarkdown::render('doc/car_analysis.Rmd')"

# render analysis report and save it as a pdf document
doc/car_analysis.pdf: doc/car_analysis.Rmd doc/references.bib
	Rscript -e "rmarkdown::render('doc/car_analysis.Rmd', 'pdf_document')"

clean:
	rm -rf data/csv/cleaned_data.csv data/csv/processed_data.csv data/figures/car_distribution.png data/figures/coefficient_graph.png data/figures/cross_val.png data/figures/feature_coeffs.png doc/car_analysis.pdf doc/car_analysis.html