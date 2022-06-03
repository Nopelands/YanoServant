import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv
from dice_parser import dice_parser

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

r_help = "Rolls dice, formatting follows !r XdY(+N(+ZdK+M(...)))\n\nWhere X and Z are the number of dice to be rolled, " \
         "Y and K are the number of sides of the rolled dice, N and M are modifiers and expressions inside " \
         "parenthesis are optional. "


@bot.command(name='r', help=r_help)
async def roll_dice(ctx, query_string):
    try:
        response = dice_parser(query_string)
    except:
        print(sys.exc_info()[0])
        response = "Unexpected Error"
    await ctx.send(response)

bot.run(token)
