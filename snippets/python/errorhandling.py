import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Error handling for a command that raises an error
@bot.command()
async def divide(ctx, num1: int, num2: int):
    try:
        result = num1 / num2
        await ctx.send(f'The result is: {result}')
    except ZeroDivisionError:
        await ctx.send("You can't divide by zero!")
    except ValueError:
        await ctx.send("Please provide valid numbers.")

# Error handling for a specific command error
@divide.error
async def divide_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to provide all the required arguments.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please provide valid numbers.")
    else:
        # Handle other errors
        await ctx.send(f"An error occurred: {error}")

# Event handler for on_ready event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
