# SteamGameTime

SteamGameTime 是一个用于获取 Steam 用户游戏时间的小工具。它使用 Steam API 来获取用户拥有的游戏信息，并将游戏名称及其对应的游戏时间保存到 Excel 文件中。

## 功能

- 使用 Steam API 获取用户拥有的游戏信息。
- 筛选用户游戏时间不为 0 的游戏。
- 将游戏名称和游戏时间保存为 Excel 文件，方便查看和分析。

## 安装

1. 克隆本仓库或下载项目的 ZIP 压缩包。
2. 安装所需的依赖库。运行以下命令：

shell

复制

```
pip install -r requirements.txt
```

## 配置

在运行 SteamGameTime 之前，需要进行一些配置。

1. 获取 Steam API 密钥：
   - 前往 [Steam 开发者门户](https://steamcommunity.com/dev/apikey) 创建一个 Steam API 密钥。
   - 将您的 Steam API 密钥保存到名为 `mysteamapi.env` 的文件中。示例：`STEAM_API_KEY=your_api_key_here`。
2. 配置 Steam ID：
   - 打开 `config.txt` 文件，并将您的 Steam ID（例如：76561197960287930）复制到文件中。

## 运行

运行 SteamGameTime 的步骤如下：

1. 打开命令行终端，导航到项目目录。
2. 运行以下命令：

shell

复制

```
python SteamGameTime.py
```

1. 程序窗口将打开，并显示以下选项：
   - "打开配置"：用于配置 Steam API 密钥和 Steam ID。
   - "运行主程序"：获取用户游戏时间并将其保存到 Excel 文件中。
2. 点击 "打开配置" 按钮，输入您的 Steam API 密钥和 Steam ID，然后点击 "保存配置"。
3. 点击 "运行主程序" 按钮，程序将获取您的游戏时间并将其保存到名为 `game_data.xlsx` 的 Excel 文件中。

## 注意事项

- 请确保您已安装 Python 和所需的依赖库。
- 请确保您的 Steam API 密钥和 Steam ID 配置正确。
- 如果遇到任何问题，请确保您的网络连接正常，并检查错误消息以获取更多信息。

希望这份简单的 README 文档能够帮助您了解并使用 SteamGameTime 工具。如有任何疑问或问题，请随时提问或联系作者。祝您使用愉快！
