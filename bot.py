import discord
from fonksiyonlar import *
from dsb import rakam,islem
import os,random
from yeni import *

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()
async def random_mem(ctx):
    img_list = [file for file in os.listdir('images') if file.endswith(('png', 'jpg', 'jpeg'))]
    if img_list:
        img = random.choice(img_list)
        with open(f'images/{img}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("Görüntü bulunamadı.")


bot.run("1")
