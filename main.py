import discord
from discord.ext import commands
import random
import time
import audioread

from quote import *
from apod import *
from weather import *
from translate import *
from ocr import *
from thispersondoesntexist import *
from wikipedia import *

prefix = '!'
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

@bot.event
async def on_message_delete(message):
    print(" DELETED  : ", message)

@bot.command()
async def setprefix(ctx, prefix):
    """Changes the bot prefix"""
    bot.command_prefix = prefix
    await ctx.send("Prefix set to \"" + prefix + "\"")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("ERROR : " + str(error))
    if "Command" in str(error) and "is not found" in str(error):
        await ctx.send("Enter \" " + str(bot.command_prefix) + "help\" for available commands")

@bot.command()
async def quote(ctx):
    """Fetch a random quote"""
    await ctx.send(get_quote())

@bot.command()
async def apod(ctx):
    """Fetch the NASA Astronomical Picture Of the Day"""
    with open(get_explanation(),'r') as file:
        explanation = file.readline()
    embed = discord.Embed(
        title = "Astronomical Picture Of the Day",
        description = explanation,
        color = discord.Color.blue()
    )
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/918px-NASA_logo.svg.png")
    embed.set_image(url=get_picture_hdurl())
    embed.set_footer(text="https://apod.nasa.gov/apod/astropix.html")
    await ctx.send(embed=embed)

@bot.command()
async def weather(ctx, city, country="ca"):
    """Fetch the Weather for a corresponding location."""
    out = format_weather(city, country).split("\n")
    embed = discord.Embed(
        title = out[0] + "\t" + f":flag_{country}:",
        color = discord.Color.blue()
    )
    if out[1] == "    Error : city not found":
        embed.add_field(name="Error",value="City not found")
        await ctx.send(embed=embed)
    else:
        for i in range(len(out)-3):
            pair = out[i+2].split(":")
            embed.add_field(name=pair[0], value=pair[1], inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def translate(ctx, message, target="en"):
    """Translate from a language to another."""
    await ctx.send(" Translation to " + target + " : " + get_translate(message, target))

@bot.command()
async def tpdne(ctx):
    """Fetch a thispersondoesnotexist.com image."""
    await ctx.send(file=discord.File(get_tpdne_picture()))

@bot.command()
async def ocr(ctx, image_url):
    """Performs OCR on image."""
    await ctx.send(get_ocr_text(image_url))

@bot.command()
async def wikipedia(ctx, search, numberResults=3):
    """Returns wikipedia top results for a string"""
    out = get_results(search, numberResults).split("\n")
    embed = discord.Embed(
        title = out[0] + "\t" + f":mag_right:",
        color = discord.Color.blue()
    )
    for i in range(numberResults):
        embed.add_field(name=out[i*3+2], value=out[i*3+3], inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_voice_state_update(member: discord.Member, before, after):
    if member.guild.id == 691785070020919347:   # Custom guild id (remove for all guilds)
        if member == bot.user:
            return
        if before.channel == after.channel:
            return
        if after.channel is None:
            return
        vc = await member.voice.channel.connect()
        audio_source = "audio\welcome.mp3"
        audio = discord.FFmpegPCMAudio(executable="ffmpeg/ffmpeg.exe", source=audio_source)
        time.sleep(0.5)
        vc.play(audio)
        time.sleep(2)
        await vc.disconnect()

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

try:
    with open("keys/DiscordToken.txt", "r") as file:
        token = file.read()
    bot.run(token)
except FileNotFoundError:
    print("Discord Bot token couldn't be found in \"keys/DiscordToken.txt\"")

