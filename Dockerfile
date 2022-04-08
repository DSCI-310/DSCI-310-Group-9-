FROM jupyter/scipy-notebook:b418b67c225b

COPY . .

# pytest v7.0.1
RUN conda install -c conda-forge/label/cf202003 pytest=7.0.1 
# numpy v1.22.3
RUN conda install -c conda-forge/label/cf202003 numpy=1.22.3
