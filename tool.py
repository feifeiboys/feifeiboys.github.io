import random
import json
strs='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
res=random.choices(strs,k=10)
res=''.join(res)

# 生成随机字符串并保存在config.json中
with open('config.json','r',encoding='utf-8') as f:
    config=json.loads(f.read())
config['pywfnID']=res
with open('config.json','w',encoding='utf-8') as f:
    f.write(json.dumps(config))
