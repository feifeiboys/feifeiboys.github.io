管道/重定向 将一个命令的输出作为另一个命令的输入

## 使用jupyter
### 在学校机房
学校机房没有公网IP，因此需要xshell做端口映射才能使用
```shell
jupyter lab --no-browser --port=2029 #使用无浏览器模式，端口可任意设置
```
然后在xhell，文件、当前会话属性、隧道、添加里添加配置

然后就可以在本机浏览器中使用了

## ssh传输文件
```
scp 本地文件 用户名@ip:文件夹
```

## 换源
1. 在清华大学镜像搜索ubuntu
2. 选择对应的版本 查看版本号：`cat /etc/issue`
3. 备份原本的源 `sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup`
4. 修改源文件 `sudo vim /etc/apt/sources.list`，替换为镜像内容
5. 更新源命令：`sudo apt update`，`sudo apt upgrade`


> 如果这时出现无法解析国内的域名，一般来说是dns出错了
```
vim /etc/resolv.conf
nameserver 8.8.8.8
```

## 作业
作业(Job)是shell管理的进程(每个job都有一个关联的PID)，每个作业会被分配一个线性job ID。
有两种形式的作业:

- Foreground: 当你在终端窗口输入命令，这个命令将会占据终端窗口，直到命令执行完成， 这是一个前台Job
- Background: 当你在命令后面添加& 符号，命令将不会占据终端窗口(你可在shell prompt继续输入)，这是一个后台Job

`jobs`命令可以列出所有的job


## 用户管理
添加用户 
```shell
useradd username
useradd -m username #ubutun
```
指定/修改密码
```shell
passwd username
```
查看用户信息
```shell
id username
```
切换用户
```shell
su -username
exit/logout #返回原用户
```
查看当前用户
```
whoami
```

## 文件管理
重命名文件
```
mv 旧名 新名
```
下载文件
```
wget 文件链接
```