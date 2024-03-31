# SteamGameTime

SteamGameTime is a tool for retrieving Steam user game time. It uses the Steam API to fetch information about the games owned by a user and saves the game names and corresponding playtime to an Excel file.

## Features

- Retrieves information about games owned by a user using the Steam API.
- Filters out games with playtime of 0.
- Saves game names and playtime to an Excel file for easy viewing and analysis.

## Installation

1. Clone the repository or download the project's ZIP archive.
2. Install the required dependencies by running the following command:

```shell
pip install -r requirements.txt
```

## Configuration

Before running SteamGameTime, some configuration steps need to be performed.

1. Obtain a Steam API key:
   - Go to the [Steam Developer Portal](https://steamcommunity.com/dev/apikey) and create a Steam API key.
   - Save your Steam API key in a file named `mysteamapi.env`. Example: `STEAM_API_KEY=your_api_key_here`.

2. Configure the Steam ID:
   - Open the `config.txt` file and copy your Steam ID (e.g., 76561197960287930) into the file.

## Usage

To run SteamGameTime, follow these steps:

1. Open a command-line terminal and navigate to the project directory.
2. Run the following command:

```shell
python SteamGameTime.py
```

3. The program window will open, displaying the following options:
   - "Open Configuration": Use this option to configure your Steam API key and Steam ID.
   - "Run Main Program": Fetches your game time and saves it to an Excel file.
   - "1658914566@qq.com": Click this button to copy the author's contact information to the clipboard.

4. Click the "Open Configuration" button, enter your Steam API key and Steam ID, and click "Save Configuration".
5. Click the "Run Main Program" button, and the program will retrieve your game time and save it to an Excel file named `game_data.xlsx`.

## Notes

- Make sure you have Python installed along with the required dependencies.
- Double-check that your Steam API key and Steam ID are configured correctly.
- If you encounter any issues, ensure that your internet connection is stable and check the error messages for more information.

We hope this simple README document helps you understand and use the SteamGameTime tool effectively. If you have any questions or concerns, please feel free to ask or contact the author. Enjoy using SteamGameTime!
