from apps.info.commands import InfoCommands

def setup(bot):
    bot.add_cog(InfoCommands(bot))