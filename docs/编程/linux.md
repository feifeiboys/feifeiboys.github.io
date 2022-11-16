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


## 用户管理
### 添加用户 
```shell
useradd username
useradd -m username #ubutun
```
### 指定/修改密码
```shell
passwd username
```
### 查看用户信息
```shell
id username
```
### 切换用户
```shell
su -username
exit/logout #返回原用户
```
### 查看当前用户
```
whoami
```