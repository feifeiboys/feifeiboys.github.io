## 添加内核
首先要有一个环境下载jupyterlab
```
conda install jupyterlab
```
然后要为指定的虚拟环境添加内核
```
conda install -n envName ipykernel
```
在虚拟环境中将内核添加到jupyterlab中
```
conda install nb_conda_kernels 
```