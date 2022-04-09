FROM jupyter/scipy-notebook:b418b67c225b

USER root

#for R-markdown
RUN conda install -c conda-forge/label/cf201901 r-base=4.1.2
# Install required dependencies for R Markdown
RUN conda install -c conda-forge r-knitr=1.38
RUN conda install -c r r-rmarkdown=2.13
RUN conda install -c conda-forge r-bookdown=0.25
RUN conda install -c conda-forge r-reticulate=1.24

# pytest v3.2.2
RUN conda install -c conda-forge/label/cf202003 pytest=3.2.2

COPY . .



