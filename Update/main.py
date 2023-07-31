import wget
import os,sys
import time

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

root = tk.Tk()

def show():
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        # 更新画面
        root.update()
        time.sleep(0.01)

Label = ttk.Label(root,text="初始化中").pack()
progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
progressbarOne['maximum'] = 100
progressbarOne['value'] = 0
progressbarOne['length'] = 200
show()

with open("cg.txt",'r',encoding = 'utf-8') as f:
    path = f.read()

os.remove(path+'MayDOS0.1_System.py')
wget.download("https://buelie.github.io/MayDOS/main.py",path)
os.rename("main.py",path+"MayDOS0.1_System.py")

root.mainloop()
