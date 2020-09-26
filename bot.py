import os

import discord
from dotenv import load_dotenv
from random import randint

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Bad bot':
        response = "*IMMUNE*"
        await message.channel.send(response)
    if message.content == "!help":
        response = "This bot supports only one roll at a time\n\nTo roll dice, use the following format: !XdY(" \
                   "+N)\n\nWhere X is the number of rolls, Y is the number of sides and N is the modifier(optional). "
        await message.channel.send(response)
    elif message.content[0] == '!':
        comando = message.content[1:]
        try:
            extra = 0
            if "+" in comando:
                comando_info = comando.split('+')
                comando = comando_info[0]
                extra = int(comando_info[1])
            results = ""
            total = extra
            dice_info = comando.split('d')
            response = "Formating Error"
            for i in range(0, int(dice_info[0])):
                roll = randint(1, int(dice_info[1]))
                results = results + str(roll) + ", "
                total += roll
                response = "You rolled " + str(total) + " (" + results[0:-2] + ")."
                if len(response) > 2000:
                    response = "You rolled " + str(total) + " (Discrete dice limit exceeded)."
        except:
            response = "Formating Error\nUse !help to get help"
        await message.channel.send(response)


client.run(token)
