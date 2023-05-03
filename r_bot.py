import random

import discord
from discord import app_commands
from discord.ext import commands
import os

secret_code = os.getenv('RB_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


class db(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync()
        self.synced = True
        print('Bot is Online')


bot = db()
tree = app_commands.CommandTree(bot)


@tree.command(name='help', description='provides information about bot function')
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('Select user in server that you would like the bot to roast.\n'
                                            'A randomly selected phrase will be displayed along with the users name.')


@tree.command(name='roast', description='select user in server and a random roast '
                                        'will be selected for them adn displayed')
async def self(interaction: discord.Interaction, user: discord.User):
    roasts = ['puts the milk in before the cereal',
              'sleeps with socks on',
              'smells kinda funny',
              'cant read',
              'cant ride a bike',
              'eats soup with a fork',
              'cant drive',
              'peaked in middle school',
              'has a face literally no one could love',
              'looks like they arent allowed near school zones',
              'has cooties',
              'cant tie their own shoes',
              'is a fringe friend',
              'has food allergies (loser)',
              'cant count past 5']
    phrase = random.choice(roasts)
    await interaction.response.send_message(f'{user} {phrase}')


def run_Roast_bot():
    bot.run(secret_code)


run_Roast_bot()
