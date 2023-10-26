# WSL
## 迁移目录
> wsl默认的位置是在c盘，我们可以将其迁移到其他盘

1 查看已经安装的linux发行版
```
wsl --list --verbose
```
2 导出系统
```
wsl --export Ubuntu D:\wsl-ubuntu
# 即 wsl --export <系统名> <导出目录>
```
3 删除系统
```
wsl --unregister Ubuntu
```
4 导入系统到指定位置
```
wsl --import Ubuntu D:\WSL2_Ubuntu D:\wsl-ubuntu --version 2
# wsl --import <系统名> <安装位置> <tar文件目录> WSL版本号
```
5 设置默认用户
```
Ubuntu config --default-user fly
```
## 修改主机名
wsl里ubuntu的主机名与电脑的`设备名称`是相同的，在电脑属性中`重命名这台电脑`即可

## 使用jupyter
在wsl中直接执行juoyter lab不太行

1. 建立浏览器连接
```bash
sudo ln -s /mnt/c/Program\ Files\ \(x86\)/Microsoft/Edge/Application/msedge.exe /usr/bin/edge
```
用如下命令验证：
```bash
edge www.baidu.com
```
能打开说明软连接建立成功

2. 配置jupyterlab

（1）查看是否存在 /home/<username>/.jupyter/jupyter_lab_config.py，若不存在，在Ubuntu shell中执行
```
jupyter lab --generate-config
```
来生成配置文件

（2）修改 jupyter_lab_config.py

打开配置文件，修改如下内容
```python
c.ServerApp.use_redirect_file = False
# 注意不要有空格(吃过大亏)
```
然后添加如下内容：
```python
import webbrowser
webbrowser.register('edge',None,webbrowser.GenericBrowser('/usr/bin/edge'))
c.NotebookApp.browser = 'edge'
```


## 限制内存占用

如果不加限制的话，wsl在运行程序是会占用很多电脑内存，导致电脑很卡。

输入如下命令可以查看linux内存的占用情况
```bash
free -h --giga
```
在c盘电脑用户下创建`.wslconfig`文件，写入：
```
[wsl2]
memory=3GB
```
即可将wsl的占用内存限制为3GB

## 网络问题
> wsl的网络默认情况下是和本地电脑关联的，即/etc/resolv.conf中的nameserver是自动生成的，但这样有时候会导致上不了网（具体原因不清楚），但是可以通过一下方式来避免

- 修改wsl.conf文件
```shell
[network]
generateResolvConf = false
```

- 修改etc/resolv.conf文件
```conf
nameserver = 8.8.8.8
```
