pyvista的学习

## 获取场景中的actor
plotter.renderer.actors

实例化对象的时候大多都是ployData对象，添加到场景后获取的是Actor对象，包含polyData对象
plotter.add_mesh()会返回一个actor对象，该函数的name参数就是actor的name

大多数属性都可以用actor对象来改变

点击场景中一个物体的时候返回的却是一个polyData对象，这就尼玛挺离谱的

## 在jupyter显示3D
```python
pyvista.global_theme.jupyter_backend = 'pythreejs'
```