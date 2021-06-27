import importlib
from core import config

bot = config.BOT

@bot.event
async def on_ready():
    """
    Initializes bot and all application modeules specified in config
    """
    for extension in config.STARTUP_COGS:
        try:
            importlib.import_module(extension)
            bot.load_extension(extension)
            extension = extension.replace('apps.', '')
        except Exception as e:
            exception = f'Could not load {extension}\n{e}'

config.BOT.run(config.TOKEN)