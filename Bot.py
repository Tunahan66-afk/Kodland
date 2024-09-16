import discord
from discord.ext import commands, tasks
import os, random
from bot_console import gen_pass

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='-', intents=intents)

activities = [
    discord.Game(name = "By Tunahan!"),
    discord.Activity(type=discord.ActivityType.listening, name = "Hizmetinizde!"),
    discord.Activity(type=discord.ActivityType.watching, name = "Sunucu Güvenliğini Sağlıyor!")
]


statuses = [
    discord.Status.online,
    discord.Status.idle,
    discord.Status.dnd,
]

@tasks.loop(minutes = 5)  
async def update_status():
    activity = random.choice(activities)
    status = random.choice(statuses)
    await bot.change_presence(activity=activity, status=status)
    print(f'Aktiflik durumu ve kullanıcı durumu değiştirildi: {activity}, {status}')

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı!')
    update_status.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "Merhaba" in message.content.lower():
        await message.channel.send("Aleyküm Selam!")
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "pet sise" in message.content.lower():
        await message.channel.send("450 Yıl!")
    if "metal sise"in message.content.lower():
        await message.channel.send("100 Yıl!")
    if "cam sise"in message.content.lower():
        await message.channel.send("4500 Yıl!")
    await bot.process_commands(message)

@bot.command()
async def sifre(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def emoji(ctx):
    await ctx.send()

@bot.command()
async def yazitura(ctx):
    yazi = "Yazı", "Tura"
    money = random.randint(1, 2)
    if money == 1:
        return("Yazı")
    elif money == 2:
        return("Tura")

@bot.command()
async def remoji(ctx):
    emoji = [":crown:", ":eyes:", ":heart:", ":zap:"]
    return random.choice(emoji)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    resim_adi = random.choice(os.listdir('images'))
    with open(f'images/{resim_adi}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, limit: int):
    if limit < 1 or limit > 200:
        await ctx.send("1 ile 200 arasında bir sayı girin.")
        return
    
    deleted = await ctx.channel.purge(limit=limit)
    await ctx.send(f"**{len(deleted)}** *mesaj silindi.*", delete_after=2)


bot.run("MTI3NzY3NDM0MDU3NzQ0Mzk0MQ.G4gpg1.yOtkEEpl7fYa1hFBAqsjMFj7cimsBy2oPzHZKs")
