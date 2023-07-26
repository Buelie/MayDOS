import os
import time
import json
import time
import sys

class JsonFile:
    """
    读取/写入JSON文件的类
    Read方法是读写JSON文件
    Write方法是写入JSON文件
    """
    def __init__(self,path) -> None:
        self.path = path

    def Read(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = json.load(f)
            f.close()
        return Data

    def Write(self):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.dumps(f)
            f.close()
        return Data

    def FileRead(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = f.read()
            f.close()
        return Data

if os.path.isdir('disk/') == False:
    os.makedirs('disk')
if os.path.isdir('disk/C/') == False:
    os.makedirs('disk/C')
if os.path.isfile('disk/C/ad.txt') == False:
    with open('disk/C/ad.txt','w',encoding='utf-8') as f:
        f.write(" ___  ____                   ______      ___     ______   \n\
|_  ||_  _|                 |_   _ `.  .'   `. .' ____ \\  \n\
  | |_/ /    .--.   _ .--.    | | `. \\/  .-.  \\| (___ \\_| \n\
  |  __'.  / .'`\\ \\[ `.-. |   | |  | || |   | | _.____`.  \n\
 _| |  \\ \\_| \\__. | | | | |  _| |_.' /\\  `-'  /| \\____) | \n\
|____||____|'.__.' [___||__]|______.'  `.___.'  \\______.' \n\
                                                          ")
        f.close()
if os.path.isfile('disk/C/config.json') == False:
    CFG_config = {"versions":"v4.1.15 pro 21H3A","MCode":0}
    with open('disk/C/config.json','w',encoding='utf-8') as f:
        f.write(json.dumps(CFG_config,sort_keys=True, indent=4, separators=(',', ':')))
        f.close()
if os.path.isfile('disk/C/user.json') == False:
    with open('disk/C/user.json','w',encoding='utf-8') as f:
        f.write(json.dumps("",sort_keys=True, indent=4, separators=(',', ':')))
        f.close()

with open('disk/C/ad.txt','r',encoding='utf-8') as f:
    print(f.read())
time.sleep(1)

cfg = JsonFile('disk/C/config.json').Read()
print("\n\n版本:"+cfg["versions"]+"      版权所有©KonDOS")
print()
print("================== KonDOS安装程序 ==================")
if cfg["MCode"] == 0:
    for i in range(1, 101):
        print("\r", end="")
        print("安装系统中: {}%: ".format(i), "█" * (i // 2), end="") #
        sys.stdout.flush()
        time.sleep(0.02)

if cfg["MCode"] == 0:
    while True:
        username = input("设置您的用户名:")
        password = input("设置您的密码:")
        if username == '':
            print("[KonDOS]:用户名不能为空！！！")
            time.sleep(0.5)
            if password == '':
                print('[KonDOS]:密码不能为空！！！')
        elif username != '' and password != '':
            UserCfg_Dict = {"Name":f'{username}-0',"password":[password]}
            with open('disk/C/config.json','w',encoding='utf-8') as f:
                f.write(json.dumps(UserCfg_Dict,sort_keys=True, indent=4, separators=(',', ':')))
                f.close()
            CFG_config = {"versions":"v4.1.15 pro 21H3A","MCode":1}
            with open('disk/C/config.json','w',encoding='utf-8') as f:
                f.write(json.dumps(CFG_config,sort_keys=True, indent=4, separators=(',', ':')))
                f.close()
            break
"""
if cfg["MCode"] == 2:
    pass
if cfg["MCode"] == 3:
    pass
if cfg["MCode"] == 4:
    0_0x000001 = input("请选择操作:\n1.启动KonDOS\n2.退出安装引导")
    if 0_0x000001 == '1':
        CFG_config = {"versions":"v4.1.15 pro 21H3A","MCode":5}
        with open('disk/C/config.json','w',encoding='utf-8') as f:
            f.write(json.dumps(CFG_config,sort_keys=True, indent=4, separators=(',', ':')))
            f.close()
    elif 0_0x000001 == '2':
        quit()
    else:
        print('不是有效的选项！')
"""
if cfg["MCode"] == 5:
    pass

print("您已完成系统初始化设置,正在为您自动跳转中...\n")
for i in range(1, 101):
    print("\r", end="")
    print("跳转中(初始化系统中): {}%: ".format(i), "█" * (i // 2), end="") #
    sys.stdout.flush()
    time.sleep(0.02)

print("\n跳转完成，已退出OOBE！\n")
os.system("filedos.py")
time.sleep(5)
