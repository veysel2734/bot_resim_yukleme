import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

a=random.randint(1,100)

@bot.command()

async def rakam(ctx):
    await ctx.send(a)

@bot.command()
async def islem(ctx):
    sayi1=random.randint(1,10)
    sayi2=random.randint(10,20)
    taplam=sayi1+sayi2
    await ctx.send(f"{sayi1} + {sayi2} = {taplam}")




@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)




bot.run("1")

