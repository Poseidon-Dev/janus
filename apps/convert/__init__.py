from apps.convert.conn import ConversionConn
from apps.convert.events import ConvertEvents

def setup(bot):
    bot.add_cog(ConvertEvents(bot))