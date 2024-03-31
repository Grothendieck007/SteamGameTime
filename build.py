import PyInstaller.__main__

if __name__ == '__main__':
    PyInstaller.__main__.run([
        'SteamGameTime.py',    # 替换为您的主入口文件名
        '--onefile',           # 打包为单个可执行文件
        '--add-data', 'config.txt;.',  # 包含config.txt文件
        '--add-data', 'mysteamapi.env;.',  # 包含mysteamapi.env文件
        '--add-data', 'Main.py;.'  # 包含Main.py文件
    ])