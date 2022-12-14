## tensorboard
以监控loss为例：
```python
# 首先导入模块
from torch.utils.tensorboard import SummaryWriter
# 然后实例化模块，自己指定数据存储的路径
writer = SummaryWriter('./board')
# 在训练的过程中可以向其中写入数据
writer.add_scalar('totalR', totalR, global_step=None, walltime=None)
```

## 可视化框架
- PytorchViz