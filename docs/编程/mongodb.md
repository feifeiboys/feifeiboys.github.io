## 安装mongodb服务
进入官网，下载tgz压缩包，解压即可

## 运行服务
### 通过命令行启动
```shell
~/mongodb/bin/mongod --port=27017 --dbpath=database/data --logpath=database/log/mongodb.log --bind_ip=0.0.0.0 --fork
```
- dbpath和logpath要手动创建
- fork指后台运行
## 通过配置文件启动
```yaml
systemLog:
	destination: file
	path: mongodb/log/mongod.log # log pathlogAppend: true
storage:
	dbPath: mongodb/data # data directory
	engine: wiredTiger #存储引擎
journal:               #是否启用journal日志
	enabled: true
net:
	bindIp: 0.0.0.0
	port: 27017 # port
processManagement:
	fork: true
```
```shell
mongod -f xxx.conf
```

## 关闭mongodb服务
1.通过命令行
```shell
启动命令 --shutdown
```
2.进入mongoshell
```js
use admin
db.shutdown()
```

## 安全认证
### 创建管理员账号
```shell
# 切换到admin库
use admin
# 创建管理员
db.createUser({user:"userName",pwd:"userPwd",roles:["root"]})
# 查看所有用户信息
show users
# 删除用户
db.dropUser("userName")
```

### 以安全模式启动
```shell
启动命令 --auth #Run with security
```

## 连接数据库
MongoDB Compass
```
mongodb://用户名:shi.密码@ip地址:端口/
```