import discord
from discord.ext import commands
from bilgiler import *
import random 
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def çevre(ctx):
    await ctx.send("Selam! Hangi konuda yardımcı olabilirim?")
@bot.command()
async def pil(ctx):
    await ctx.send("Pilin doğru kullanılması için:")
    await ctx.send("* Suya veya toprağa atılmamalı, atılırsa karışabilir.")
    await ctx.send("* Tek kullanımlı yerine şarj edilebilir piller kullanılmalıdır.")
    await ctx.send("* Pilin sıradan çöp yerine pil geri dönüşüm kutusuna atılmalıdır.")
    with open(f'sorunfotolari/pilgd.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()
async def geri_dönüşüm_atıkları_nereye_atılmalı(ctx):
    with open(f'sorunfotolari/bilgi1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    await ctx.send("Kağıt:")
    await ctx.send("* Karton kutu, karton")
    await ctx.send("* Gazete kağıdı, kağıt")
    await ctx.send("* Kitap, dergi")
    await ctx.send("-")
    await ctx.send("Cam:")
    await ctx.send("* Cam şişe")
    await ctx.send("* Bardak")
    await ctx.send("-")
    await ctx.send("Organik:")
    await ctx.send("* Et ürünleri")
    await ctx.send("* Süt ürünleri")
    await ctx.send("* Meyveler, sebzeler")
    await ctx.send("-")
    await ctx.send("Plastik:")
    await ctx.send("* Plastik şişe")
    await ctx.send("* Plastik poşet")
    await ctx.send("* Disk (Plastikse)")
    await ctx.send("-")
    await ctx.send("Metal:")
    await ctx.send("* Teneke kutu")
    await ctx.send("* Metal araç. Örneğin kaşık, bıçak veya makas.")
    await ctx.send("* Disk (Metalse)")

@bot.command()
async def poşet(ctx):
    await ctx.send("* Tek kullanımlı plastik poşet yerine kumaş poşet kullanmalıyız.")
    await ctx.send("* Plastik poşetler suya veya karaya atılmamalıdır.")
    await ctx.send("* Eğer suya atılırsa su kirlenebilir, su canlıları tarafından yenilip zehirlenebilir.")
    await ctx.send("* Eğer karaya atılırsa toprak kirlenebilir, doğa zarar görebilir. Ayrıca plastiklerin çürümesi yıllar alır.")
    with open(f'sorunfotolari/bilgi2.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def fabrika(ctx):
    await ctx.send("* Fabrika dumanları filtrelenmelidir.")
    await ctx.send("* Fabrikalar şehir merkezinin dışında kurulmalıdır.")
    await ctx.send("* Fabrika atıklarının suya veya karaya atılmamalıdır.")
    with open(f'sorunfotolari/fabgercekleri.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def gıda_israfı(ctx):
    await ctx.send("* Bir şeyler alırken yiyeceğimiz kadar almalı, fazlası israftır.")
    await ctx.send("* Eğer yemeği bitiremezseniz aç insanları ve aç olan hayvanlara veriniz.")
    await ctx.send("* Hadi onlar da yok, o zaman komposto yapabilirsiniz.")
    with open(f'sorunfotolari/bilgi3.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def geri_dönüşüm_video(ctx):
    with open(f'sorunfotolari/geridonusumvido.mp4', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def kağıt(ctx):
    await ctx.send("* Kağıtın arka sayfası boş bırakılmamalı, her tararı doldurulmalıdır.")
    await ctx.send("* Kağıtlar geri dönüşüm çöplerine atılmalıdır.")
    await ctx.send("* Kağıtlar ve kartonlar değerlendirilip yeni şeyler yapılabilir.")
    with open(f'sorunfotolari/bilgi4.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    await ctx.send("'https://www.youtube.com/watch?v=XvgHNH_n8JQ' sitesinden öbür bilgilere bakabilirsiniz.")

bot.run(token)