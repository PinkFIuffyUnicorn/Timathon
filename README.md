# Discord Bot Setup

## Prerequisites
1. You have Python >= 3.8 installed
2. Have Python (>=3.8) in path

## Discord Developer Portal

1. Go to https://discord.com/developers (sign in)
2. Click create application in the upper right corner
3. Click "Bot" tab and click "Add Bot"
4. At the bottom of the page add the necessary permissions (Administrator)
5. Invite the bot to your server by going to this URL: https://discordapp.com/oauth2/authorize?client_id=ID_HERE&scope=bot&permissions=0
Change "ID_HERE" with your bots ID (General Information → CLIENT ID)
6. Get your token by going to the Bot tab and copying the token (you will need this later to run this bot)

## Setting up your environment

1. Download the necessary files from GIT (Timathon/discordBot/)
2. Run the following in the Command Line Terminal (Administrator):
```py
pip install discord
pip install requests
pip install random-username
pip install youtube-dl
pip install youtube-search
```

3. Change the "YOUR_TOKEN_HERE" part of the code (bot.py) with your previously gotten token (refer to point 6. in "Discord Developer Portal" instructions)

## Running the bot
1. Move to where you have your bot.py file and run the following: `python bot.py`
