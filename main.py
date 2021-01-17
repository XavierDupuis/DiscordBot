import discord
from discord.ext import commands
import random

from quote import *
from apod import *
from weather import *

prefix = '-'
description = '''Custom Kirbo Bot'''
bot = commands.Bot(command_prefix=prefix, description=description)
#bot.remove_command("help")
#@bot.group(invoke_without_command=True)
#async def help(ctx):
#    author = ctx.message.author
#    await ctx.send(author)

@bot.event
async def on_ready():
    print('------------------------------------')
    print('     ===      BOT READY     ===     ')
    print('Name     : ', bot.user.name)
    print('#        : ', bot.user.discriminator)
    print('ID       : ', bot.user.id)
    print('Prefix   : ', bot.command_prefix)
    print('------------------------------------')
    nameActivity = prefix + "help for more info"
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=nameActivity))


@bot.command()
async def setprefix(ctx, prefix):
    """Changes the bot prefix"""
    bot.command_prefix = prefix
    await ctx.send("Prefix set to \"" + prefix + "\"")

@bot.command()
async def quote(ctx):
    """Fetch a random quote"""
    await ctx.send(get_quote())

@bot.command()
async def apod(ctx):
    """Fetch the NASA Astronomical Picture Of the Day"""
    await ctx.send("https://apod.nasa.gov/apod/astropix.html")
    await ctx.send(file=discord.File(get_picture()))
    with open(get_explanation(),'r') as file:
        await ctx.send(file.readline()) 

@bot.command()
async def weather(ctx, city, country="ca"):
    """Fetch the Weather for a corresponding location"""
    await ctx.send(format_weather(city, country))

################################################################
#@bot.command()
#async def add(ctx, left: int, right: int):
#    """Adds two numbers together."""
#    await ctx.send(left + right)
#    
#@bot.command()
#async def roll(ctx, dice: str):
#    """Rolls a dice in NdN format."""
#    try:
#        rolls, limit = map(int, dice.split('d'))
#    except Exception:
#        await ctx.send('Format has to be in NdN!')
#        return
#
#    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#    await ctx.send(result)
#
#@bot.command(description='For when you wanna settle the score some other way')
#async def choose(ctx, *choices: str):
#    """Chooses between multiple choices."""
#    await ctx.send(random.choice(choices))
#
#@bot.command()
#async def repeat(ctx, times: int, content='repeating...'):
#    """Repeats a message multiple times."""
#    for i in range(times):
#        await ctx.send(content)
#
#@bot.command()
#async def joined(ctx, member: discord.Member):
#    """Says when a member joined."""
#    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
#
#@bot.command()
#async def server_info(ctx):
#    """server_info"""
#    await ctx.send(bot.get_guild)
#
#@bot.group()
#async def cool(ctx):
#    """Says if a user is cool.
#
#    In reality this just checks if a subcommand is being invoked.
#    """
#    if ctx.invoked_subcommand is None:
#        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))
#
#@cool.command(name='bot')
#async def _bot(ctx):
#    """Is the bot cool?"""
#    await ctx.send('Yes, the bot is cool.')
#####################################################################

file = open("keys/DiscordToken.txt", "r")
token = file.read()
file.close()
bot.run(token)
