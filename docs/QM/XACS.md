
> 厦门原子计算套件

## XMVB
这个软件是干啥的？


### 计算$LiF$
平衡距离为1.5埃

activate space应该在inactivate之后

F2的例子：
```py
F2 VBSCF with 3 structures

$CTRL
STR=FULL  # 根据指定的activate space自动生成所有VB结构
NAO=2 NAE=2  # 包含两个轨道和两个电子的activate space
ISCF=5 # 指定算法
IPRINT=3 # 打印信息等级
ORBTYP=HAO FRGTYP=SAO # VB轨道用片段描述
INT=LIBCINT # 积分工具
BASIS=CC-PVDZ # 基组类型
$END

$FRAG  # 片段 fragment
1*6  # 6个片段，每个片段一个原子
SPZDXXDYYDZZ 1
SPZDXXDYYDZZ 2
PXDXZ 1
PXDXZ 2
PYDYZ 1
PYDYZ 2
$END

$ORB # 轨道 orbital
1*10 # 有10个轨道，每个轨道由一个片段组成
1
2
1
2
3
4
5
6
1
2
$END

$GEO
F 0.0 0.0 0.0
F 0.0 0.0 1.4
$END
```
不明白的点
- activate space, activate electrons
- fragment
- VB orbital