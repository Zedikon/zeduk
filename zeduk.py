import discord
import random
import time
import asyncio
import datetime

zeduk = discord.Client()

# time
delta = datetime.timedelta(hours=3, minutes=0)
t = (datetime.datetime.now(datetime.timezone.utc) + delta)
nowtime = t.strftime("Дата: %d.%m.%Y Время: %H:%M:%S")

# random
randoms = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#embed
embed = discord.Embed(
    title='',
    color=discord.Color.red())

@zeduk.event
async def on_ready():
    print('You login as: {0}!'.format(zeduk.user))
    while True:
          await zeduk.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"за {len(zeduk.guilds)} серверами"))

    @zeduk.event
    async def on_message(message):
        if message.author == zeduk.user:
            return
# ping
        if message.content.startswith("z!ping"):
            await message.channel.send(f':alarm_clock:Ping: {0}'.format(zeduk.latency),)
        if message.content.startswith("z!Ping"):
            await message.channel.send(':alarm_clock:ping: {0}'.format(zeduk.latency))
# avatar
        if message.content.startswith("z!ava"):
            embed.add_field(name=f'Аватарка:', value=message.author.avatar_url)
            await message.channel.send(embed=embed)
        if message.content.startswith("z!Ava"):
            await message.channel.send(f":camera_with_flash:Your avatar:")
            await message.channel.send(message.author.avatar_url)
# time
        if message.content.startswith("z!time"):
            embed.add_field(name=f'Время:', value=nowtime)
            await message.channel.send(embed=embed)
        if message.content.startswith("z!Time"):
            embed.add_field(name=f'Время:', value=nowtime)
            await message.channel.send(embed=embed)
# guild
        if message.content.startswith("z!server"):
            await message.channel.send(f"Server: {len(zeduk.guilds)}")
# random
        if message.content.startswith("z!Random"):
            embed.add_field(name=f':8ball:Рандом', value=random.choice(randoms))
            await message.channel.send(embed=embed)
        if message.content.startswith("z!random"):
            embed.add_field(name=f':8ball:Рандом', value=random.choice(randoms))
            await message.channel.send(embed=embed)
#newserver
@zeduk.event
async def on_guild_join(guild):
    category = guild.categories[0]
    channel = category.channels[0]
    embed.add_field(name=f'Новый сервер!', value="Привет! Спасибо что добавили меня на сервер! Пропишите z!help что бы посмотреть мой функционал!")
    await newguild.send(embed=embed)

# newmember
@zeduk.event
async def on_member_join(member):
    hello = ["приветсвую тебя на нашем сервере!", "добро пожаловать на наш сервер!"]
    embed.add_field(name=f'Привет!', value=random.choice(hello))
    await member.send(embed=embed)


zeduk.run('твой токен')
