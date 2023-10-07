import discord
from discord.ext import commands
from discord_interactions import CommandContext

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Register a slash command
@bot.command()
async def hello(ctx: CommandContext):
    await ctx.send("Hello, this is a slash command!")

# Run the bot with your token
if __name__ == "__main__":
    bot.run('YOUR_BOT_TOKEN')
