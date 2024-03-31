import tkinter as tk
from tkinter import messagebox
import webbrowser

def save_config(api_key, steam_id):
    # 将API密钥保存到.env文件
    with open("mysteamapi.env", "w") as file:
        file.write(f"STEAM_API_KEY={api_key}")

    # 将Steam ID保存到配置文件
    with open("config.txt", "w") as file:
        file.write(steam_id)

def load_config():
    try:
        with open("config.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def configure_environment():
    window = tk.Tk()
    window.title("配置运行环境")
    window.geometry("300x150")
    print("配置运行环境窗口已打开")

    api_key_label = tk.Label(window, text="Steam API密钥:")
    api_key_label.pack()
    api_key_entry = tk.Entry(window)
    api_key_entry.pack()

    steam_id_label = tk.Label(window, text="Steam ID:")
    steam_id_label.pack()
    steam_id_entry = tk.Entry(window)
    steam_id_entry.pack()

    def save_configuration():
        api_key = api_key_entry.get()
        steam_id = steam_id_entry.get()

        save_config(api_key, steam_id)

        messagebox.showinfo("配置已保存", "运行环境配置已保存成功。")
        print("配置已保存")
        window.destroy()

    save_button = tk.Button(window, text="保存配置", command=save_configuration)
    save_button.pack()

    # 重新加载配置文件
    steam_id_entry.insert(0, load_config())

    window.mainloop()