## ssh传输文件
```
scp 本地文件 用户名@ip:文件夹
```

## gunicorn
部署fastapi服务
```
gunicorn main:app -b 0.0.0.0:8000  -w 4 -k uvicorn.workers.UvicornH11Worker --daemon
```
获取 Gunicorn 进程树
```
pstree -ap | grep gunicorn
```
杀死 Gunicorn 服务
```
kill -HUP ID
kill -9 ID
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