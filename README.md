
# Car Evaluation

Contributors/Authors: Allan, Fred, Ayasha, Zhe


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


## Dockerfile instructions

Inside directory with Dockerfile do this to build the image:  
`docker build -t dsci-group-9 .`  

After building, do this to start the Jupyter Server on local port `8888`:  
`docker run --rm -p 8888:8888 dsci-group-9`

-OR-  

Pull image from dockerHub:  
`docker pull zhangfred8/dsci-310-group-9:latest`  

After pulling image:  
`docker run --rm -p 8888:8888 zhangfred8/dsci-310-group-9`  



[CoC for this project](CODE_OF_CONDUCT.md)
