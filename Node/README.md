# Discord Bot in NodeJS

[![N|Solid](https://pbs.twimg.com/card_img/1706660851640635392/ekbkjgsu?format=jpg&name=4096x4096)](https://nodesource.com/products/nsolid)

# Description
Beginner's Type

## Features

- **Modular Structure**: Commands are organized into a "Moderation" cog for easy management and scalability.

- **Event Handling**: The bot triggers an "on_ready" event upon startup, indicating its readiness to serve your server.

- **Moderation Commands**:
  - `clear`: Clear a specified number of messages from the current channel.
  - `ban`: Ban a user from the server with a specified reason and send an embed confirmation message.
  - `kick`: Kick a user from the server with a specified reason and send an embed confirmation message.
  - `unban`: Unban a user by providing their user ID and send an embed confirmation message.

- **Permission Checks**: All moderation commands include permission checks to ensure that only authorized users can execute them, enhancing server security.

- **Rich Embeds**: Confirmation messages for moderation actions are sent as visually appealing rich embeds, providing essential information.

- **Cog Setup**: Included is a setup function that simplifies adding the Moderation cog to your Discord bot.


## Tech

- [Node] -
- [discord.js] -

## Installation

Bot requires [Node](https://nodejs.org/en).

Install the dependencies.

```sh
npm install discord.js
```

Creating files

```sh
touch main.js .env
```

setting up environment variable...

```env
TOKEN=<your_bot_token>
```

## Development

Want to contribute? Great!
