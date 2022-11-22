# FastApi


## 调试
```
uvicorn main:app --reload
```
- main：main.py 文件（一个 Python "模块"）。
- app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
- --port: 指定端口
- --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
## 部署