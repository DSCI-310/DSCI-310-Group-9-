
# Car Evaluation

Contributors/Authors: Allan, Fred, Ayasha, Zhe


## List of Dependencies



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
