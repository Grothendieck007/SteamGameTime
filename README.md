SteamGameTime
SteamGameTime是一个用于获取Steam用户游戏时间的小工具。它使用Steam API来获取用户拥有的游戏信息，并将游戏名称及其对应的游戏时间保存到Excel文件中。

功能
使用Steam API获取用户拥有的游戏信息。
筛选用户游戏时间不为0的游戏。
将游戏名称和游戏时间保存为Excel文件，方便查看和分析。
安装
克隆本仓库或下载项目的ZIP压缩包。

安装所需的依赖库。运行以下命令：

basic
复制
pip install -r requirements.txt
配置
在运行SteamGameTime之前，需要进行一些配置。

获取Steam API密钥：

前往 Steam开发者门户 创建一个Steam API密钥。
将您的Steam API密钥保存到名为mysteamapi.env的文件中。示例：STEAM_API_KEY=your_api_key_here。
配置Steam ID：

打开config.txt文件，并将您的Steam ID（例如：76561197960287930）复制到文件中。
运行
运行SteamGameTime的步骤如下：

打开命令行终端，导航到项目目录。

运行以下命令：

复制
python SteamGameTime.py
程序窗口将打开，并显示以下选项：

"打开配置"：用于配置Steam API密钥和Steam ID。
"运行主程序"：获取用户游戏时间并将其保存到Excel文件中。
点击"打开配置"按钮，输入您的Steam API密钥和Steam ID，然后点击"保存配置"。

点击"运行主程序"按钮，程序将获取您的游戏时间并将其保存到名为game_data.xlsx的Excel文件中。

注意事项
请确保您已安装Python和所需的依赖库。
请确保您的Steam API密钥和Steam ID配置正确。
如果遇到任何问题，请确保您的网络连接正常，并检查错误消息以获取更多信息。
希望这份简单的README文档能够帮助您了解并使用SteamGameTime工具。如有任何疑问或问题，请随时提问或联系作者。祝您使用愉快！
