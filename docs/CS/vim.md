# vim
> 再服务器上直接编辑文件需要用到vim，所以还是好好学学vim吧

适合vim使用的键盘 HHKB Poker2 *贼特么贵*


vim file 打开文件
:wq 保存退出

vim有四种模式
- 正常模式 esc
- 插入模式 i a o
- 命令模式 : /
- 可视模式 v

## 正常模式
### 编辑
- x 删除
- c 删除并进入插入模式
- dd 删除一行
- dt{char} 删除到指定字符
- y 复制 yarn；yy 复制一行
- p 粘贴 past
- u 撤销 undo

123

### 移动
光标移动 h左 j下 k上 l右
单词移动 **w**(下一个单词开头) e(下一个单词结尾) **b**(上一个单词) 大小的忽略空格等
行间移动 f{char} ; t , F
水平移动 0(行首Home) ^(行首非空白0w) $(行尾End) g\_(行尾非空白)
页面移动 gg/G(移动到文件开头/结尾) ctrl+0 快速返回 H/M/L(屏幕开头/中间/结尾) ctrl+u/f 上/下翻页 zz 把当前行放到屏幕中间

gi 回到最后编辑的位置继续编辑

## 插入模式
ctrl+h 删除上一个字符；ctrl+w 删除上一个单词；ctrl+u 删除当前行 backspace其实都能做到，终端中也可以使用

## 命令模式
:% 操作全部
set nu 显示行号

## 可视模式
正常模式下按v进入visual选择
使用V选择行
使用ctrl+v方块选择 windows下和粘贴冲突

## 多文件操作
几个重要概念：
- Buffer 文件的缓冲区
- Window 可视化的分割区域
- Tab 将窗口分组

:e file 打开文件
:ls 列出当前当开的文件
:b n 跳转到第n个文件
:sp 水平分割窗口
:vs 垂直分割窗口 vertical split

### 窗口切换
以Ctrl+w作为前缀
- w 在窗口间循环切换
- h/j/k/l 切换到左/下/上/右边的窗口
- H/L 移动窗口

## 文本对象
```
[number]<command>[text object]
```
- number 次数
- command 命令，例如d c y
- text object 文本对象，例如单词w，句子s，段落p

文本范围 i(inner) a(around)
> 举个例子：当想要修改括号中的内容时，可以用`ci(`


## 复制粘贴
正常模式
y d p 可配合可视模式使用 yy 复制一行
插入模式

> vim中使用的是寄存器而不是系统剪切板
默认使用的是无名寄存器，可以使用多个寄存器
"{register} 前缀可以指定寄存器
:reg 查看寄存器，用+可以复制到系统剪切板

## 补全
Ctrl+n ctrl+p 补全单词
Ctrl+x+f 补全文件名
Ctrl+x+o 补全代码，需要开启文件类型检查，安装插件

## 主题配色
:colorscheme 显示当前主题
:colorscheme ctrl+d 显示所有主题


## 配置
> 我的vim我做主
创建并编辑 ~/.vimrc
### 常用设置
设置显示行号等
:h option-list 显示所有可以的设置
### vim映射
- 设置一下leader键，let mapleader="," 通常为逗号或空格
- 很复杂
### vimscript脚本
一般人用不到

## 插件
### 插件管理器
**vim-plug** 在github中下载
在vimrc中写入：
```
call plug#begin()
Plug '插件路径'
cal plug#end()
```
然后source一下vimrc文件 (好像不能source?!)

最后执行`PlugInstall`

### 搜索插件
网站: Vim Awesome

- 修改启动界面 vim-startify
- 状态栏美化 vim-airline
- 增加代码缩进条线 indentline
- 好看的主题 vim-hybrid

### 文件目录树 nerdtree
:NERDTree 开启目录树
