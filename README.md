
# DSCI310 Group 9 Project: Car Evaluation

## Project Team
This project is managed and built by the group 9 of the UBC DSCI310 offered in 2021WT2. The contributors/authors of this project include Allan, Fred, Ayasha, and Zhe. The instructors of the course who are also the supervisor of this project include Tiffany and Giuseppe.

## Project Summary
Written in Python language, this project aims to train a Logistic Regression model provided in the scikit-learn package to predict the car price based on the door count, passenger capacity, trunk space, safety, class, and maintenance. Our training employs 10-fold cross validation to tune the hypter-parameters to avoid overfitting while making the best use of our training set. The dataset used for training is the Car Evaluation dataset retrived from the UC Irvine Machine Learning Repository. 

## Porject Execution
The code for this project is included in the data_analysis.ipynb in the repositoy. In order to properly run and get reproducable result, please use the Dockerfile we created and attached in this repository to construct a container with the same environment we used for development, then run the jupyter notebook inside the container. Please follow the instructions presented here to set up the container.

Inside directory with Dockerfile do this to build the image:  
`docker build -t dsci-group-9 .`  

After building, do this to start the Jupyter Server on local port `8888`:  
`docker run --rm -p 8888:8888 dsci-group-9`

-OR-  

Pull image from dockerHub:  
`docker pull zhangfred8/dsci-310-group-9:latest`  

After pulling image:  
`docker run --rm -p 8888:8888 zhangfred8/dsci-310-group-9`  

Failing to run the code inside the speicifed container may lead to unexpected result due to the versioning of the imported libraries. The dependencies of this project are also listed below for reference. 

## List of Dependencies
Package Name              | Version     | Channel
--------------------------|-------------|----------
pandas                    | 1.3.5       | conda-forge
jupyterlab                | 3.2.7       | conda-forge
jupyterlab-git            | 0.34.1      | conda-forge
jupyterlab-spellchecker   | 0.7.2       | conda-forge
jupytext                  | 1.13.6      | conda-forge
jupyterlab-lsp            | 3.10.0      | conda-forge
jupyter-lsp-python        | 1.5.1       | conda-forge
scikit-learn              | 1.0.0       | conda-forge

## License
Please note that this open-source project is licensed under the **MIT License**. For the details, please refer to the LICENSE.md in this repository.

