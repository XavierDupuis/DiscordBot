import discord
from discord.ext import commands
import random

from quote import *
from apod import *

prefix = '-'
description = '''Custom Kirbo Bot'''
bot = commands.Bot(command_prefix=prefix, description=description)

#@bot.command()
#async def setprefix(self, ctx, *, prefixes=""):
#    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
#    await ctx.send("Prefixes set!")

@bot.event
async def on_ready():
    print('------------------------------------')
    print('Logged in as')
    print('Bot Name : ', bot.user.name)
    print('Bot ID   : ', bot.user.id)
    print('------------------------------------')
    nameActivity = prefix + "help for more info"
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=nameActivity))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def quote(ctx):
    """Fetch a random quote"""
    q = get_quote()
    await ctx.send(q)

@bot.command()
async def apod(ctx):
    """Fetch the NASA Astronomical Picture Of the Day"""
    await ctx.send(file=discord.File(get_picture()))
    with open(get_explanation(),'r') as file:
        await ctx.send(file.readline()) 

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def server_info(ctx):
    """server_info"""
    await ctx.send(bot.get_guild)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


file = open("token.txt", "r")
token = file.read()
file.close()
bot.run(token)
