# python 绘图
> 绘图可是个技术活，导师说过，文章中的一张图顶上几十句话(大概是这个意思)

不太会用orange绘图，感觉还是自己用代码的方式绘图简单一些

在py脚本里画图比在jupyter里画图快多了，画的图比较大的时候还是直接用脚本画图吧
## 子图左上角的编号
我们绘制科研论文的时候，很多情况下一个大图分为很多小图，这是后我们就需要在每个子图的左上角写上编号，可以通过一下代码来实现：
```python
ax.text(-0.1, 1.05, '(f)', transform=ax.transAxes, size=markSize)
```
该函数的详细用法可以自己去查就不详细记录了
## 保存图片时去除边缘的空白
有时候保存图片的时候边缘会有很大的空白，甚至有一些内容会显示不全，或者显示模糊，用以下代码可以解决问题
```python
fig.savefig('image.png',bbox_inches='tight',dpi=300)
```
## 调整子图间距离
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)

## 使用`SciencePlots`：论文绘图工具包
项目地址: https://github.com/garrettj403/SciencePlots

使用该工具包

## 图片大小
在绘制期刊上的图片时，全幅一般15cm，半幅一般7.5cm，而matplotlib图片大小的单位是inchi(英寸)，一厘米=0.4英寸，所以全幅图片宽度应为6，半幅宽度应为3，单个图片宽度七厘米，高度六厘米

总结：
- 宽度=$7.5*0.4*n$  
- 高度=$6*0.4*n$  
- dpi=300  
- wSpace=0.2,hSpace=0.3

## 字体大小
matplotlib中字体大小的默认单位是像素，而word中的单位是磅，1磅=4/3像素
## 显示绘制svg
就目前我所知的，PIL不能直接导入svg图像，所以需要借用一个库cairosvg
直接`pip install cairosvg`即可，但是这个库需要电脑上有cairo，这就很麻烦了，毕竟windows下安装软件是一件挺费劲的是，但还好咱有wsl
wsl下`sudo apt-get install python-cairo`就行了(不得不说linux就是好用，尤其是安装软件的时候)
然后就可以用命令行将svg转为png了:`cairosvg image.svg -o image.png -s 5`,-s的参数是指缩放的大小，虽然svg图片任意缩放不失真，但还是有默认大小的，如果不修改导出的图片可能不清楚
## 关于latex
有时候需要在图上显示公式，但是今天突然遇到个问题`No pages of output.`，发现这其实还是使用了scienceplots导致的，但是怎么解决还是不清楚。所以还是使用自己设置字体来绘图吧。