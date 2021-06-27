import discord, os, platform, asyncio
from discord.ext import commands
import re

convertions = {
   'km': [0.621371, 'miles'], 'kms': [0.621371, 'miles'], 'kph': [0.621371, 'miles'],  
   'mile': [1.06934, 'km'], 'miles': [1.06934, 'km'], 'mph': [1.60934, 'km'],
   'inch': [2.54, 'cm'], 'inches': [2.54, 'cm'],
   'cm': [0.393701, 'inches'], 'cms': [0.393701, 'inches'],
   'foot': [0.3048, 'meters'], 'feet': [0.3048, 'meters'],
   'meter': [3.28084, 'feet'], 'meters': [3.28084, 'feet'],
   'pound': [0.453592, 'kg'], 'pounds': [0.453592, 'kg'], 
   'lb': [0.453592, 'kg'], 'lbs': [0.453592, 'kg'],
   'kilogram': [2.20462, 'lbs'], 'kilograms': [2.20462, 'lbs'], 'kg': [2.20462, 'lbs'],'kgs': [2.20462, 'lbs'],
}

class ConvertEvents(commands.Cog, name='convertion_events'):

    def __init__(self, bot):
      self.bot = bot
      self.convertions = convertions
       
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            values = self.values_to_convert(message)
            if values:
                for value in values:
                    conversions = self.convert_to_cousin(value)
                    await message.channel.send(conversions)

    def values_to_convert(self, message):
        """
        Returns a list of tuples of containing the values and current measurements
        of any message within the server as long as the measurement is within
        the supported types
            ex: [('180', 'lbs), ('6', 'feet')]
        """
        if any(val in message.content for val in self.convertions.keys()):
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
        """
        Converts a (unit, method) tuple into a human readable conversion
        """
        conversion = round(self.convertions.get(value[1])[0],2) * round(float(value[0]),2)
        conversion = f'{value[0]} {value[1]} = {conversion} {self.convertions.get(value[1])[1]}'
        return conversion
