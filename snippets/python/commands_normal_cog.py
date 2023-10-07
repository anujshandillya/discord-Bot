import discord
from discord.ext import commands

# Create a custom bot class that inherits from commands.Bot
class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix)
        self.remove_command('help')  # Optional: Remove the default help command

    # Event handler for on_ready event
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

# Create an instance of your bot with a prefix
bot = MyBot(command_prefix='!')

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
bot.run('YOUR_BOT_TOKEN')
