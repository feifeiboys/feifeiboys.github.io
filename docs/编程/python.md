# Python

> 记录一些常用python技术以及在学习中的笔记

## 坑爹事
使用多线程传参时，`args=(p,)`，参数元组内一定要加一个逗号，今天在传参时传入了一个字符串，字符串中的每一个字符都被当成一个参数穿进去了，导致参数超了，太特么坑了

## vscode颜色含义
在使用vscode进行python编程的时候，程序会根据代码中不同的类型来显示不同的颜色

据我观察，在默认的黑色模式下
|颜色|cn|en|
|---|---|---|
|蓝色|变量<br>属性<br>参数|variable<br>property<br>parameter|
|黄色|函数<br>方法|function<br>method|
|绿色|类|class|
|紫色|保留字|-|
|白色|任意|Any|

## lru_cache 数据缓存
在python中，有时候需要频繁调用一个函数，而且传入的参数都一样，为了避免浪费计算时间，可以将相同的计算参数所得到的结果缓存起来，这样再次调用函数的时候可以直接返回缓存结果
```python
from functools import lru_cache,cached_property
```
其中`lru_cache`是用来装饰函数或类方法，`cached_property`是用来装饰类属性

## python embeddable 嵌入式python
当做好程序想给别人用时，打包是个麻烦事，因为打包之后的程序会很大，所以嵌入版本的python是一个好选择

## cython