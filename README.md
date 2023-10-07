# Discord Bot
[![N|Solid](https://pbs.twimg.com/card_img/1706660851640635392/ekbkjgsu?format=jpg&name=4096x4096)](https://nodesource.com/products/nsolid)

## Introduction
This is a rudimentary bot with plans for future feature enhancements as we progress.

## Features 
**COMMANDS**

- `.help` : It used to provide users with information about the bot's commands and how to use them. This command is used to display a list of available commands or provide details about a specific command.
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

- `.level`: It is a command that allows users to check their or other users' levels within a leveling system. To implement a leveling system in your Discord bot, you'll need to track users' experience points (XP) and levels.
  
-  `.levelreset`: It is a command used to reset a user's level and experience points (XP) back to a certain starting point or zero.

- `.me`: It allows users to view their own profile information or personal statistics within a server or community. This command can provide users with information about their username, avatar, roles, join date, or any other relevant data you want to display.

- `.mem`: It used to provide users with information about the another member's  personal statistics within a server or community.

- `.play`: It  is  used to make the bot join a voice channel and play audio, such as music or sound effects.

- `.join`: It is used to make the bot join a voice channel in a Discord server. This command allows the bot to connect to a voice channel so that it can participate in voice-related activities, such as playing music, relaying audio, or responding to voice commands.

- `.leave`: It is used to make the bot leave a voice channel in a Discord server. This command allows the bot to disconnect from a voice channel when it's no longer needed.

- `.ping`: It is a common and simple command that allows you to measure the bot's latency or response time. Users can invoke the command, and the bot responds with the time it takes for a message to be sent and received.
  

## Technology used

- [Python] 
- [discord.py] 

## Installation

This Bot requires [Python](https://www.python.org/downloads/) for functioning.

How to install the dependencies?

```sh
pip install discord.py
```

How to create files?

```sh
touch main.py .env
```

How to set up environment variables?

```env
TOKEN=<your_bot_token>
```

## Development

Interested in making a contribution? Fantastic!
