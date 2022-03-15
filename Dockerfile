FROM jupyter/scipy-notebook:b418b67c225b

COPY . .

# pytest v7.0.1
RUN conda install -c conda-forge/label/cf202003 pytest
# numpy v1.22.3
RUN conda install -c conda-forge/label/cf202003 numpy