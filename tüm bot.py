import discord
import random
import os
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

    


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
async def topla(ctx, x = 0 , y = 0):
    await ctx.send(x + y)

@bot.command()
async def çarp(ctx, a = 0 , b = 0):
    await ctx.send(a * b)

@bot.command()
async def böl(ctx, a = 0 , b = 0):
    if a % b > 0:
        await ctx.send("bu sayı bölünemiyor")
    else:
        await ctx.send(a / b)

@bot.command()
async def faktoriyel(ctx, n = 0):
    if n == 0 or n == 1:
        await ctx.send(1)
    else:
        x = 1
        while n > 1:
            x = x*n
            n = n-1             
        await ctx.send(x)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    with open("picture/resim1.png" , 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def fox(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)





def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    '''fox komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem_oran(ctx):
    olasiliklar = [0.1, 0.3, 0.5,]
    img_name = random.choices(os.listdir('picture'), weights=olasiliklar, k=1)[0]
    with open(f'dosya yolu/{img_name}', 'rb') as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)

@bot.command()
async def random_pokemon(ctx):
    random_pokemon_id = random.randint(1, 800)  
    url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}'
    res = requests.get(url)
    data = res.json()
    image_url = data['sprites']['front_default']
    await ctx.send(data["forms"][0]["name"])
    await ctx.send(image_url)

bot.command()
async def pokemon(ctx, pokemon_name = "charmander"):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        image_url = data['sprites']['front_default']
        await ctx.send(image_url)
    else:
        await ctx.send(f"{pokemon_name} adında bir Pokemon bulunamadı.")



bot.run("BOT_TOKEN")
