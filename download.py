"""
下载文件并解压到当前文件夹
"""
import requests
from pathlib import Path
import json

def get_localID():
    """获取程序的本地id"""
    cwd=Path.cwd()
    configFile=cwd/'config.json'
    if configFile.exists:
        with open(configFile,'r',encoding='utf-8') as f:
            config=json.loads(f.read())
            return config['id']
    else:
        with open(configFile,'w',encoding='utf-8') as f:
            f.write('{}')
            return None

root='https://vkceyugu.cdn.bspapp.com/VKCEYUGU-f551f9c1-1083-4ceb-8724-fb1c75629b6f/'
res=requests.get('https://static-f551f9c1-1083-4ceb-8724-fb1c75629b6f.bspapp.com/config.json')

# 检测文件夹内有没有python有没有python38

if res.status_code==200: #如果请求成功
    config=res.json()
    if config['id']!=get_localID(): # 如果网络的id与本地的id不一样就更新
        zipRes=requests.get(f'{root}{config["id"]}.zip')
        if zipRes.status_code==200:
            with open('pywfn.zip','wb') as f:
                f.write(zipRes.content)
        else:
            print('更新失败')
