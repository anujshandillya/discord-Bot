# Discord Bot
[![N|Solid](https://pbs.twimg.com/card_img/1706660851640635392/ekbkjgsu?format=jpg&name=4096x4096)](https://nodesource.com/products/nsolid)

# Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
    - [Commands](#commands)
3. [Technology Used](#technology-used)
4. [Installation](#installation)
    - [Install Python](#install-python)
    - [Install Dependencies](#install-dependencies)
    - [Create Files](#create-files)
    - [Set Up Environment Variables](#set-up-environment-variables)
    - [Load Environment Variables](#load-environment-variables)
    - [Bot Initialization](#bot-initialization)
5. [Contribution](#contribution)



## Introduction
Welcome to our Discord bot project! This bot is designed as a versatile tool with plans for future feature enhancements as we continue to develop it.


## Features 
### COMMANDS
- `.help` :Use this command to access information about the bot's available commands and how to use them. You can request a list of all commands or details about a specific command. Here's a sample output:
```sh
LevelSystem:
  level      
  levelreset 
Me:
  me         
  mem        
Music:
  join       
  leave      
  play       
Ping:
  ping       
​No Category:
  help       Shows this message
  setprefix  

Type .help command for more info on a command.
You can also type .help category for more info on a category.
```

- `.level`: Check your or other users' levels within our leveling system. We've implemented an XP and level tracking system to enhance your Discord experience.
  
-  `.levelreset`: Reset a user's level and XP back to a certain starting point or zero with this command.

- `.me`: View your own profile information or personal statistics within our server or community. This command provides details about your username, avatar, roles, join date, and more.

- `.mem @user`: Retrieve personal statistics about another member within our server or community.

- `.play`:  Make the bot join a voice channel and enjoy audio playback, including music and sound effects.

- `.join`: Summon the bot into a voice channel to participate in voice-related activities such as music playback or voice commands.

- `.leave`: Dismiss the bot from a voice channel when it's no longer needed.

- `.ping`: Measure the bot's latency or response time with this simple command. It provides you with the time it takes for a message to be sent and received.

- `.ban @user`: Use this command to ban a user from your server. Replace `@user` with the mention of the user you want to ban, and you can optionally provide a reason for the ban. The reason helps in documenting the ban's purpose.

- `.unban @user`: Unban a previously banned user from your server. This command is useful for reversing a ban when necessary. You only need to specify the user's mention to unban them.

- `.clear`: Clear a specified number of messages in a channel. This command helps in keeping your server's chat clean and free from clutter. Only users with appropriate permissions can use this command.

- `.kick @user`: Kick a user from your server. Similar to the ban command, you can replace `@user` with the mention of the user you want to kick and provide an optional reason for the action.


## Technology used

- [Python] : The primary programming language used for bot development.
- [discord.py] : The Python library that enables interaction with the Discord API.

## Installation
To get started with our Discord bot, follow these steps:
### **Install Python** 
 Ensure you have Python installed on your system. You can download it from here [Python's official website](https://www.python.org/downloads/).

### **Install Dependencies**
  - Install the required Python packages using the following command:
```sh
pip install discord.py
```
  - FFmpeg Installation (For Audio/Video Features)

To use audio and video features in your Discord bot, you'll need to install FFmpeg, a multimedia framework that allows you to manipulate audio and video data. Follow these steps to install FFmpeg:

- Windows

1. Visit the FFmpeg download page: [FFmpeg Downloads](https://ffmpeg.org/download.html).

2. Scroll down to the "Windows" section and click the "Windows Builds by Zeranoe" link.

3. Download the latest version of FFmpeg by clicking the link under "Release."

4. Extract the downloaded ZIP file to a location on your computer.

5. Add the path to the FFmpeg executable to your system's PATH environment variable. To do this:
   - Search for "Environment Variables" in the Windows Start menu.
   - Click "Edit the system environment variables."
   - Click the "Environment Variables" button.
   - Under "System variables," find the "Path" variable and click "Edit."
   - Click "New" and add the path to the directory containing the FFmpeg executable (e.g., `C:\path\to\ffmpeg\bin`).
   - Click "OK" to save your changes.

6. To verify the installation, open a Command Prompt and run the following command:

```sh
ffmpeg -version
```   
### **Create Files**
 Create the necessary files for your bot, including main.py and .env (for environment variables): 

```sh
touch main.py .env
```

### **Set Up Environment Variables**
Open the .env file and define your environment variables. The most crucial variable is your Discord bot token:

```env
DISCORD_TOKEN=your_bot_token_here
```
Replace `your_bot_token_here` with your actual Discord bot token.

### **Load Environment Variables**
    Load the environment variables in your Python code using a library like `python-dotenv`. Make sure to install it:
    
```sh
pip install python-dotenv
```
Then, use the following code at the start of your main.py or equivalent:
```py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
```
###  **Bot Initialization**

     In your bot's code, use the DISCORD_TOKEN variable to authenticate your bot with Discord. Here's an example snippet:
     
 ```py
     import discord
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Create a Discord client
client = discord.Client()

# Bot functionality and event handlers go here

# Run the bot
client.run(TOKEN)
```

Remember to keep your .env file secure and never share your bot token publicly.

With these installation steps completed, your Discord bot will be up and running, ready to serve your community. Feel free to customize and expand the bot's features to enhance your Discord server's experience.

## Contribution 

Interested in making a contribution? Fantastic!
