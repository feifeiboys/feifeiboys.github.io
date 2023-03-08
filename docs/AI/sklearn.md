## scikit-learn的一般流程
### 1.获取数据集
### 2.数据预处理
### 3.数据集拆分
```python
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size = 0.3,random_state=1)
```
### 4.定义并训练模型
```python
# 拟合模型
model.fit(X_train, y_train)
# 模型预测
model.predict(X_test)
# 模型参数
model.get_params()
# 模型得分
model.score(data_X, data_y)
```
### 5.模型的评估与选择
### 6.保存模型