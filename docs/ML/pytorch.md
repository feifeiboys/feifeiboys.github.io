## pytorch无法导入
windows下安装pytorch成功，但是无法导入，将环境变量中的`PYTHONHOME`和`PYTHONPATH`删除即可

## tensorboard
### 监控标量
> 可以将训练过程中产生的标量（损失等），动态地添加到一个图表中，并且随时查看
- 添加标量
```python
# 首先导入模块
from torch.utils.tensorboard import SummaryWriter
# 然后实例化模块，自己指定数据存储的路径
writer = SummaryWriter('./board')
# 在训练的过程中可以向其中写入数据
writer.add_scalar('totalR', totalR, global_step=None, walltime=None)
```
- 运行tensorborad
```sh
tensorboard --logdir=/path/to/board
```

## 可视化框架
- PytorchViz

## 模型参数量
```py
sum([l.numel() for l in net.parameters()])
```

## 模型の保存&加载
```py
# 保存模型
torch.save(net.state_dict(), 'net.pth')
# 加载模型
net.load_state_dict(net.load('net.pth'))
net.eval() # 测试时使用
```