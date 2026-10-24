import discord, random, os, requests, time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

tips = ["Recicla las cosas como botellas u otros", "Intenta botar cosas que no son faciles de descomponer en la basura", "Compra cosas que no hagan tanto daños al ambiente"]

@bot.command()
async def tip(ctx):
    result = random.choice(tips)
    await ctx.send(result)

@bot.command()
async def image(ctx):
    image = random.choice(os.listdir("nature"))
    with open(f'nature/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(0.2)
    await ctx.send("Esto es un ejemplo de lo que podrias hacer.")

bot.run("")
