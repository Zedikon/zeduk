import discord
import random
import time
import asyncio

zeduk = discord.Client()

# module
time_string = time.strftime("Время: %H:%M:%S")
citats = ['', '', '']
mat = [""]


@zeduk.event
async def on_ready():
    print('Вы залогинины как: {0}!'.format(zeduk.user))
    await zeduk.change_presence(activity=discord.Streaming(name="Префикс z!", url="your twitch ;)"))

    @zeduk.event
    async def on_message(message):
        if message.author == zeduk.user:
            return
# ping
        if message.content.startswith("z!пинг"):
            await message.channel.send(f':alarm_clock:Пинг: {0}'.format(zeduk.latency),)
        if message.content.startswith("z!Пинг"):
            await message.channel.send(':alarm_clock:Пинг: {0}'.format(zeduk.latency))
# avatar
        if message.content.startswith("z!ава"):
            await message.channel.send(f":camera_with_flash:Ваша аватарка:")
            await message.channel.send(message.author.avatar_url)
        if message.content.startswith("z!Ава"):
            await message.channel.send(f":camera_with_flash:Ваша аватарка:")
            await message.channel.send(message.author.avatar_url)
# time
        if message.content.startswith("z!время"):
            await message.channel.send(f"{time_string}")
        if message.content.startswith("z!Время"):
            await message.channel.send(f"{time_string} ")
# guild
        if message.content.startswith("z!сервера"):
            await message.channel.send(f"Количество серверов: {len(zeduk.guilds)}")
# random
        if message.content.startswith("z!рандом"):
            await message.channel.send(f":8ball:Вам выпало число:{random.choice(random4ik)}")
        if message.content.startswith("z!Рандом"):
            await message.channel.send(f":8ball:Вам выпало число:{random.choice(random4ik)}")
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
