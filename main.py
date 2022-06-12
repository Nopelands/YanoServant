import os
import sys
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from dice_parser import dice_parser
import logging

logging.basicConfig(level=logging.INFO)

def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    guild = os.getenv('DISCORD_GUILD')

    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        for i in bot.guilds:
            if i.name == guild:
                break

        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{i.name}(id: {i.id})'
        )

    r_help = "Rolls dice, formatting follows !r XdY( + N( + ZdK + M(...)))\n\nWhere X and Z are the number of dice to be rolled, " \
             "Y and K are the number of sides of the rolled dice, N and M are modifiers and expressions inside " \
             "parenthesis are optional. Can also subtract by replacing + with - or using negative modifiers."

    @bot.command(name='r', help=r_help, )
    async def roll_dice(ctx, *args):
        query_string = ' '.join(args)
        try:
            response = dice_parser(query_string)
        except:
            print(sys.exc_info()[0])
            response = "Unexpected Error"
        await ctx.send(response)

    tree = app_commands.CommandTree(bot)

    @tree.command(name="roll", description="rolls dice with modifiers.")
    async def slash_roll_dice(interaction: discord.Interaction):
        await interaction.response.send_message("test")

    bot.run(token)


if __name__ == '__main__':
    main()
