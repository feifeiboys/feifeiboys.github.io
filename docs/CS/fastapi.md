# FastApi


# FastAPI
## 调试
```
uvicorn main:app --reload
```
- main：main.py 文件（一个 Python "模块"）。
- app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
- --port: 指定端口
- --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
## 部署

使用的是在阿里云购买的云服务器

通过gunicorn.py的配置文件来部署

可以指定ssl证书（也是在阿里云上购买的免费的）

## pydantic
> 用于python的类型提示(type hints)，指定的数据类型可以是python语言自带的，也可以是自定义的
```python
from pydantic import BaseModel
from typing import Optional
# 自定义数据类型
class Man(BaseModel):
	name:str
	age:int
	sex:str="man" #指定默认
	height:Optional[float] #可选

data={
	"name":"fly",
	"age":18,
	"sex":"man",
	"height":1.8
}
fly=Man(**data) # 用解包的方式使用字典数据实例化类型
```

基于python类型提示来定义数据验证，序列化和文档(JSON)库

## starlette
轻量级ASGI框架/工具包，是构建高性能Asyncio服务的理想选择

ASGI服务(异步python web框架服务)：`Uvicorn`、Hypercorn、Daphne  
WSGI服务(同步python web框架服务)：uWSGI、Gunicorn

FastApi=(Pydantic+Starlette)


在服务器上可以每个项目创建一个虚拟环境(virtual env)(当包比较多的时候可能会遇到版本不兼容问题)

`路径参数`和`查询参数`
路径参数要包含在请求路径中，用{}包裹住
查询参数在url中以，在函数中直接作为参数传入 '?q=xxx'
校验的时候，路径参数用Path，查询参数用Query

一个项目可以有多个应用，每个应用在一个文件夹内，项目根目录要有一个入口文件

为每一个应用分配单独的路径，使用APIRouter

路径参数和数字验证

参数可以是枚举类型，在给定范围内选择

当路径参数是路径时，要指定参数为路径
```python
"files/{file_path:path}"
```

对请求体
> 课程进度 11/44