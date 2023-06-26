> 免费开源的分布式管理控制系统


- `工作区` 写代码
- `暂存区` 临时存储
- `本地库` 历史版本
- `远程库` 代码托管/github/gitee

本地库 git add 暂存区 git commit 工作区

## git常用命令

设置用户签名
```
git config --global user.name
git config --global user.email
```
用户签名和github或gitee的账号没有关系

初始化本地仓库
```
git init
```
查看本地库状态
```
git status
```
追踪文件（添加到暂存区）
```
git add <file>
git rm --cached <file> # 取消追踪
```
暂存区在.git目录里

提交文件（添加到本地库）
```
git commit -m "日志信息" <file>
```
查看历史版本
```
git log    # 详细
git reflog # 精简
```
HEAD是指针

版本穿梭
```
git reset --hard 版本号 # 精简的版本号
```

## git分支
查看分支
```
git branch -v
```
创建分支
```
git branch 分支名
```
切换分支
```
git checkout 分支名
```
切换分支
## 将本地项目上传到github

github
创建远程仓题
代码推送 push
代码拉取 pull
代码克隆 clone
ssh免密登录

gitee

gitlab
基于局域网的代码托管中心
