#colorama使用说明：
#Fore.xxx  前景色（字体颜色）
#Back.xxx 背景色
#Fore常用颜色：
#Fore.GREEN
#Fore.CYAN
#Fore.BLUE
#Fore.RED
#Fore.MAGENTA
#Fore.BLACK
#Fore.YELLOW
#详情请在Py控制台导入colorama并输入help(Fore)
#系统颜色表示说明：
#绿色：提示，正确
#红色：警告，错误
#黄色：警告，错误（比红色弱一点）
#浅蓝色：信息，属性
#紫红色：暂定
#黑色：无（黑色哪看得见？）

import wget
import json
import requests
import os,sys
import time
import base64
from time import sleep
from colorama import Fore, Back, init
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

if os.path.isdir('MayDOS_Login/') == False:
    os.makedirs('MayDOS_Login/')
if os.path.isdir('important/') == False:
    os.makedirs('important/')
if os.path.isdir('important/Applications') == False:
    os.makedirs('important/Applications')
if os.path.isdir('important/log') == False:
    os.makedirs('important/log')
if os.path.isdir('important/download') == False:
    os.makedirs('important/download')
if os.path.isfile('important/download/cg.txt') == False:
    path_url = os.getcwd() + "\\"
    with open('important/download/cg.txt','w') as f:
        f.write(path_url)
        f.close()

root = tk.Tk()

def show():
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        # 更新画面
        root.update()
        time.sleep(0.01)
    Update = json.loads(requests.get("https://buelie.github.io/MayDOS/config.json").text)
    code = "0.0.4"
    if Update["latest"]["default"] != code:
        Y_N_U = tkinter.messagebox.askyesno(title='更新提示',message=f'有可用更新，是否下载?\n当前版本:{code} -> {Update["latest"]["default"]}\n稍等一下，马上就好')
        if Y_N_U == True:
            if os.path.isfile('important/download/main.py'):
                os.remove("important/download/main.py")
            else:
                pass
            wget.download("https://buelie.github.io/MayDOS/Update/main.py","important/download")
            cmd_0 = r'start "自动更新" "important/download/main.py"'
            os.system(cmd_0)
            print("\n")
            quit()
        else:
            root.withdraw()
        root.withdraw()
    else:
        root.withdraw()

Label = ttk.Label(root,text="检查更新中").pack()
progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
progressbarOne['maximum'] = 100
progressbarOne['value'] = 0
progressbarOne['length'] = 200
show()

init(autoreset=True)

def cls():
    os.system('cls')

error_version_file_not_found = False
error_account_file_not_found = False

try:
    ver_open= open('important/Version.ver',mode='r')
    Ver = ver_open.readline()
except  FileNotFoundError:
    error_version_file_not_found = True

try:
    account_open = open('important/account.user',mode='r')
    account_info = account_open.readlines()

    un_username = account_info[0]
    username = un_username[0:-1]

    un_password = account_info[1]
    password = un_password[0:-1]

    account_open.close()
    
    try:
        username = str(base64.b64decode(username),'utf-8')
        password = str(base64.b64decode(password),'utf-8')
    except Exception as e:
        print(Fore.RED + 'ERROR: 账户信息加载失败，账户文件可能损坏，请尝试注销并重新注册')
        print(Fore.RED + 'ERROR_INFOMATION')
        print(e)
        sleep(10)
        quit()
    
except FileNotFoundError:
    error_account_file_not_found = True

if error_account_file_not_found == True and error_version_file_not_found == False:
    print(Fore.RED + '未注册或账户文件异常丢失')
    input('按下回车键退出...')
    quit()
elif error_version_file_not_found == True and error_account_file_not_found == False:
    print(Fore.RED + '系统版本文件被移动或异常丢失，请尝试联系我们以修复')
    input('按下回车键退出...')
    quit()
elif error_account_file_not_found  and error_version_file_not_found == True:
    print(Fore.RED + '未找到系统版本文件及账户文件')
    print(Fore.RED + '请确认是否注册并尝试联系我们')
    input('按下回车键退出...')
    quit()
    
if username == 'TEST':
    print(account_info)

print(Fore.GREEN + 'Welcome!')

while True:
    if username == 'TEST':
        print(Fore.BLUE + 'test_account_auto_login')
    else:
        print(Fore.CYAN + f'登录{username}的电脑')
    
    if username == 'TEST':
        break
    else:
        userspassword = input('密码>')

    if userspassword == password:
        print(Fore.GREEN + '密码正确')
        break
    else:
        print(Fore.RED + '密码错误！')
        pass

sleep(1)
cls()

print(Fore.GREEN + '正在准备你的MayDOS命令行......')
print(Fore.GREEN + '请输入"usebook"以打开MayDOS0.1的使用手册和帮助')
time.sleep(1.5)

while True:
    cmd = input('MayDOS/Root>>>')
    
    if cmd == 'calc':
        os.system('python important/Applications/calc.py')

    elif cmd[0:3] == 'sof':
        os.system(f'python important/Applications/{cmd[4:-1]}')

    elif cmd == "":
        pass

    elif cmd == 'usebook':
        print(Fore.GREEN + '键入"calc"以打开计算器')
        print(Fore.GREEN + '键入"close"以关闭PyDOS0.1')
        print(Fore.GREEN + '键入"notepad"以打开记事本程序')
        print(Fore.GREEN + '键入"explorer"以打开资源管理器')
        print(Fore.GREEN + '键入"cls"以清屏')
        print(Fore.GREEN + '键入"sysver"以查看系统版本')
        print(Fore.GREEN + '键入"sof <程序名称>"以打开第三方应用程序')

    elif cmd == 'close':
        quit()

    elif cmd == 'notepad':
        cls()
        os.system('python important/Applications/Notepad.py')

    elif cmd == 'explorer':
        cls()
        os.system('python important/Applications/Explorer.py')

    elif cmd == 'cls':
        cls()

    elif cmd =='sysver':
        print(f'系统版本：MayDOS{Ver}')
        print('开发：MayDOS开发团队 版权所有2023(C)')
    else:
        print(Fore.YELLOW + "未定义的指令",cmd,Fore.YELLOW + "，请输入'usebook'以查看使用手册和帮助")

root.mainloop()
