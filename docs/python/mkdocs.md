# mkdocs的使用
## 介绍
mkdocs是一个python库,可以将markdown渲染成网页,非常适合用来写博客(只有文字和图片),而且可以部署到github pages上，相当于白嫖了一个静态网站(本博客就是)
## 安装
直接用python `pip install pywfn`即可
## 创建项目
```
mkdocs new 项目名
```
## 本地调试
运行以下命令即可开启本地调试
```
mkdocs serve
```
## 部署到github
创建一个github pages项目,克隆到本地,mkdocs的项目代码复制进来
```shell
mkdocs gh-deploy
```
该命令会在本地生成一个site目录，并且其上传的github上的一个新的分支`gh-pages`

最后回到github的项目，找到setting、Page，选择github pages的source为`gh-pages`

之后就可以愉快地访问我们的博客啦