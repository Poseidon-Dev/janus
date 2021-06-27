import os
import discord
from discord.ext import commands

TESTING = False

# BOT INFO
VERSION = os.getenv('VERSION')
DESCRIPTION = """Simple Imperial/Metric Converter bot"""

# SETTINGS
BOT_PREFIX = ('!', '-')
TOKEN = os.getenv('BOT_TOKEN')
APPLICATION_ID = os.getenv('APPLICATION_ID')
INTENTS = discord.Intents.default()
BOT = commands.Bot(BOT_PREFIX, intents=INTENTS)
BOT.remove_command('help')

# CURRENT MODULES
STARTUP_COGS = [
    'apps.convert',
]

DB_LOCATION = os.getenv('DB_LOCATION')