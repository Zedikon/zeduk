import discord
import random
import time
import asyncio

zeduk = discord.Client()

# переменные
time_string = time.strftime("Время: %H:%M:%S")
random4ik = ['1', '2', "3", "4", "5", "6", "7", "8", "9", "10"]
ugadayka = ['1', '2']
citats = ['', '', '']
mat = [""]
erunda = ["лосось", "михайлов", "пятый", "2008", "ромбик", "стас", "бомбастер", "пажылой", "читос", "липтон"]


@zeduk.event
async def on_ready():
    print('Вы залогинины как: {0}!'.format(zeduk.user))
    await zeduk.change_presence(activity=discord.Streaming(name="Префикс z!", url="https://yandex.ru/?clid=22411725&0x419="))

    @zeduk.event
    async def on_message(message):
        if message.author == zeduk.user:
            return
# ping
        if message.content.startswith("z!пинг"):
            await message.channel.send(f':alarm_clock:Пинг: {0}'.format(zeduk.latency),)
        if message.content.startswith("z!Пинг"):
            await message.channel.send(':alarm_clock:Пинг: {0}'.format(zeduk.latency))
# аватарка
        if message.content.startswith("z!ава"):
            await message.channel.send(f":camera_with_flash:Ваша аватарка:")
            await message.channel.send(message.author.avatar_url)
        if message.content.startswith("z!Ава"):
            await message.channel.send(f":camera_with_flash:Ваша аватарка:")
            await message.channel.send(message.author.avatar_url)
# время
        if message.content.startswith("z!время"):
            await message.channel.send(f"{time_string}")
        if message.content.startswith("z!Время"):
            await message.channel.send(f"{time_string} ")
# сервера
        if message.content.startswith("z!сервера"):
            await message.channel.send(f"Количество серверов: {len(zeduk.guilds)}")
# тест
        if message.content.startswith("z!тест"):
# рандомное число
        if message.content.startswith("z!рандом"):
            await message.channel.send(f":8ball:Вам выпало число:{random.choice(random4ik)}")
        if message.content.startswith("z!Рандом"):
            await message.channel.send(f":8ball:Вам выпало число:{random.choice(random4ik)}")
# инфо
        if message.content.startswith("z!инфо"):
            await message.channel.send("https://sun9-11.userapi.com/5vq4ln1gHhqBxU8QYlkZAtxXzCLGuFG8qFYV5w/jmo1gEnTR9Y.jpg")
            await asyncio.sleep(2)
            await message.channel.send("**РАЗРАБОТЧИКИ БОТА: @sherifoboltus и @Hell_Strawberry**")
            await asyncio.sleep(2)
            await message.channel.send("**БОТ ЗАРЕГЕСТРИРОВАН: 8 июня 2020**")
            await asyncio.sleep(2)
            await message.channel.send("**БОТ СОЗДАН: 1 сентября 2020**")
# аноним-чат
        if message.content.startswith("."):
            await message.delete()
            await message.channel.send(f"**Кто-то сказал: {message.content}**")
# ерунда и бред
        if message.content.startswith("z!ерунда"):
            await message.channel.send(f"{random.choice(erunda)} {random.choice(erunda)}")

@zeduk.event
async def on_guild_join(guild):
    category = guild.categories[0]
    channel = category.channels[0]
    await channel.send("**привет я новый на этом сервере! мой префикс 'z!' что бы увидеть мой фунционал пропиши z!команды**")

@zeduk.event
async def on_member_join(member):
    privet = ["приветсвую тебя на нашем сервере!", "добро пожаловать на наш сервер!"]
    await member.send(f'Привет {member}! **{random.choice(privet)}**')


zeduk.run('NzE5NjQ0MDA4MTQ1NDg1OTE1.Xt6atQ.KFWBR2oUibYVrys7VF7Ip5CaRsc')
