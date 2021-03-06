import discord
from discord.ext import commands
import re

from core import config
from apps.convert import ConversionConn
class ConvertEvents(commands.Cog, name='conversion_events'):

    def __init__(self, bot):
      self.bot = bot
      self.keys = [val[0] for val in ConversionConn().keys()]
       
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            values = self.values_to_convert(message)
            if values:
                for value in values:
                    conversions = self.convert_to_cousin(value)
                    await message.channel.send(conversions)

    def values_to_convert(self, message):
        if any(val in message.content for val in self.keys):
            message_list = message.content.split()
            dataset = re.findall(r'[0-9]+', message.content)
            extracted = list(zip(
                    [val for val in message_list for data in dataset if data in val], 
                    dataset))
            values = []
            for val in extracted:
                m_index = message_list.index(val[0])
                if len(val[1]) == len(message_list[m_index]):
                    values.append((val[1], message_list[m_index+1]))

                if len(val[1]) < len(message_list[m_index]):
                    values.append(tuple(re.findall('(\d+)(\w+)', message_list[m_index])[0]))
            return values

    def convert_to_cousin(self, value):
        convert = ConversionConn().conversion(value)
        new_val = convert[0]
        if 'x' in new_val:
            new_val = round(eval(new_val.replace('x', value[0])), 2)
        else:
            new_val = round(float(new_val) * float(value[0]), 2)
        return f'{value[0]}{value[1]} = {new_val}{convert[1]}'
