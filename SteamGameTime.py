import tkinter as tk
from tkinter import messagebox
import pyperclip
import Config
import Main
import subprocess

def copy_contact_info():
    contact_info = "1658914566@qq.com"
    pyperclip.copy(contact_info)
    messagebox.showinfo("复制成功", "联系方式已复制到剪贴板")

def open_config():
    Config.configure_environment()

def run_main():
    try:
        Main.main_function()
        messagebox.showinfo("运行成功", "主程序已成功运行，请在该程序目录下获取数据文件")
    except Exception as e:
        messagebox.showerror("运行错误", "无法运行主程序，请检查SteamAPI和SteamID是否正确配置！")
        print(e)

window = tk.Tk()
window.title("SteamGameTime")
window.geometry("400x300")

title_label = tk.Label(window, text="SteamGameTime", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

open_config_button = tk.Button(window, text="打开配置", command=open_config)
open_config_button.pack(pady=10)

run_main_button = tk.Button(window, text="运行主程序", command=run_main)
run_main_button.pack(pady=10)

# 创建一个标签来显示作者名称
author_label = tk.Label(window, text="作者：拓跋无烈", font=("Arial", 12))
author_label.pack(side="bottom")

# 创建一个按钮来显示联系方式并触发复制功能
contact_button = tk.Button(window, text="1658914566@qq.com", command=copy_contact_info)
contact_button.pack(side="bottom")

window.mainloop()