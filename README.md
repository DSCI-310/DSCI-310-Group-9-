
# DSCI310 Group 9 Project: Car Evaluation

## Project Team
This project is managed and built by the group 9 of the UBC DSCI310 offered in 2021WT2. The contributors/authors of this project include Allan, Fred, Ayasha, and Zhe. The instructors of the course who are also the supervisor of this project include Tiffany and Giuseppe.

## Project Summary
Written in Python language, this project aims to train a Logistic Regression model provided in the scikit-learn package to predict the car price based on the door count, passenger capacity, trunk space, safety, class, and maintenance. Our training employs 10-fold cross validation to tune the hypter-parameters to avoid overfitting while making the best use of our training set. The dataset used for training is the Car Evaluation dataset retrived from the UC Irvine Machine Learning Repository. 

We have found that higher values of class and maintenance features decrease the value of the vehicle. While safety and the higher capacity increase the value of the car the most. It was unexpected because the positive correlation between vehicle capacity and its price as such perception can be subjective. Some people may value having more seats in a car than others due to personal preference. Moreover, we cannot use this model to discuss 
the impacts of such findings because the accuracy of the model needs to be increased a lot more before anything can be reasonably/confidently inferred 
from it. In the future, we can see if adding more features such as horsepower or branding of the car affects the value of the vehicle. It would also be 
interesting to see if introducing more categories in our target variable would increase the accuracy of the model.

## Project Execution
The code for this project is included in the car_analysis.ipynb in the repositoy. In order to properly run and get reproducable result, please use the Dockerfile we created and attached in this repository to construct a container with the same environment we used for development, then run the jupyter notebook inside the container. Please follow the instructions presented here to set up the container.

Inside directory with Dockerfile do this to build the image:  
`docker build -t dsci-group-9 .`  

After building, do this to start the Jupyter Server on local port `8888`:  
`docker run --rm -p 8888:8888 dsci-group-9`

-OR-  

Pull image from dockerHub:  
`docker pull zhangfred8/dsci-310-group-9:latest`  

After pulling image:  
`docker run --rm -p 8888:8888 zhangfred8/dsci-310-group-9`

Copy the resulting URL from the prompt that begins with,
`http://127.0.0.1:888/lab?token=<your token>`
and paste the URL into your preferred web browser to start the Jupyter notebook


Failing to run the code inside the speicifed container may lead to unexpected result due to the versioning of the imported libraries. The dependencies of this project are also listed below for reference. 

## Testing
Our project uses the `Pytest` testing framework

Once you have started the Jupyter Notebook, to run our test suite, 
run the following command in the root directory of the project:  
`python -m pytest tests/pytest/`


## List of Dependencies
Using `python 3.9.5`

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
matplot-lib               | 3.5.1       | conda-forge
pytest                    | 7.0.1       | conda-forge
numpy                     | 1.22.3      | conda-forge

## License
Please note that this open-source project is licensed under the **MIT License**. For the details, please refer to the LICENSE.md in this repository.

