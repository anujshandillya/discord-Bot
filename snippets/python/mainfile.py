import discord
from discord.ext import commands

# Create a bot instance with a prefix
bot = commands.Bot(command_prefix='!')

# Event handler for on_ready event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Greet
@bot.command()
async def greet(ctx, member: discord.Member):
    await ctx.send(f'Hello, {member.mention}!')

# Error handling for the greet command
@greet.error
async def greet_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a user to greet.")
    else:
        await ctx.send(f"An error occurred: {error}")

# Run the bot with your token
if __name__ == "__main__":
    bot.run('YOUR_BOT_TOKEN')
