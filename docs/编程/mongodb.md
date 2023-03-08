## 安装mongodb服务
进入官网，下载tgz压缩包，解压即可

## 运行服务
```shell
~/mongodb/bin/mongod --port=27017 --dbpath=database/data --logpath=database/log/mongodb.log --bind_ip=0.0.0.0 --fork
```
- dbpath和logpath要手动创建
- fork指后台运行

## 关闭mongodb服务
```shell
~/mongodb/bin/mongod --port=27017 --dbpath=database/data --shutdown
```