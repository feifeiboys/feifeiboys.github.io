# pyscf
## 构建分子
实例化一个分子对象
> https://pyscf.org/user/gto.html#

```python
from pyscf import gto
# 实例化分子
mol=gto.Mole()
# 设置分子属性

# 构建分子
mol.build()
```
可以设置的属性有：
- atom 原子类型及坐标
- basis 基组
- unit 单位

## 缩写解释
- mf,mean filed
- xc 电子密度相关泛函的缩写，它代表着交换-相关能的表达式