import discord
import random
import time
import asyncio

zeduk = discord.Client()

# time
delta = datetime.timedelta(hours=3, minutes=0)
t = (datetime.datetime.now(datetime.timezone.utc) + delta)
nowtime = t.strftime("[%d.%m.%Y %H:%M:%S]")

# random
randoms = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

@zeduk.event
async def on_ready():
    print('You login as: {0}!'.format(zeduk.user))
    await zeduk.change_presence(activity=discord.Streaming(name="Префикс z!", url="your twitch ;)"))

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
            await message.channel.send(f":camera_with_flash:Your avatar:")
            await message.channel.send(message.author.avatar_url)
        if message.content.startswith("z!Ava"):
            await message.channel.send(f":camera_with_flash:Your avatar:")
            await message.channel.send(message.author.avatar_url)
# time
        if message.content.startswith("z!time"):
            await message.channel.send(nowtime)
        if message.content.startswith("z!Time"):
            await message.channel.send(nowtime)
# guild
        if message.content.startswith("z!server"):
            await message.channel.send(f"Server: {len(zeduk.guilds)}")
# random
        if message.content.startswith("z!Random"):
            await message.channel.send(f":8ball:Random:{random.choice(randoms)}")
        if message.content.startswith("z!random"):
            await message.channel.send(f":8ball:Random:{random.choice(randoms)}")
# delete message
        if message.content.startswith("z!delete"):
            await message.delete()
#hello
@zeduk.event
async def on_guild_join(guild):
    category = guild.categories[0]
    channel = category.channels[0]
    await channel.send("**привет я новый на этом сервере! мой префикс 'z!' что бы увидеть мой фунционал пропиши z!команды**")

# newmember
@zeduk.event
async def on_member_join(member):
    privet = ["приветсвую тебя на нашем сервере!", "добро пожаловать на наш сервер!"]
    await member.send(f'Привет {member}! **{random.choice(privet)}**')


zeduk.run('your token')
