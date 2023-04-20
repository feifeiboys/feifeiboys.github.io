# gaussian
## 在linux安装gaussian
1. 创建一个`gaussian`文件夹，将压缩包`G16_C02_AVX2.tbJ`复制进去
2. 解压压缩包，得到一个`g16`的目录
```bash
tar -xvf G16_C02_AVX2.tbJ
```
3. 创建一个`scr`文件夹，用来存储临时文件
4. 设置环境变量
```bash
export g16root=$HOME/gaussian
export GAUSS_EXEDIR=$g16root/g16
export GAUSS_SCRDIR=$g16root/scr
# 这三句话写进.bashrc里面
```
source一下
```bash
source ~/.bashrc
```
5. 更改权限
```bash
chmod -R 700 $GAUSS_EXEDIR
# Linux chmod（英文全拼：change mode）命令是控制用户对文件的权限的命令
# -R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递归的方式逐个变更)
```
6. 进入g16目录，安装csh，安装gaussian16
```bash
cd $GAUSS_EXEDIR
sudo apt-get install csh # 用来调用c shell
./bsd/install

source $GAUSS_EXEDIR/bsd/g16.profile # 执行并在.bashrc中写入
```
然后就能通过`g16 <文件名>`的方式运行计算了。
