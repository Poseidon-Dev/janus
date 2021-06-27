import discord, platform
from discord.ext import commands

import core.config

class InfoCommands(commands.Cog, name='info_commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='about')
    async def about(self, ctx):
        """
        Returns some general information about Janus
        """
        embed = discord.Embed(
            title='About Janus',
            desciption='Janus General Information',
            color=0xE3E3E3,
            timestamp=ctx.message.created_at)
        embed.add_field(name="Owner", value="Poseidon#4021", inline=True)
        embed.add_field(name='Python Version', value=f'{platform.python_version()}', inline=False)
        embed.add_field(name='Janus Version', value=f'{core.config.VERSION}', inline=False)
        embed.add_field(name='Description', value=f'{core.config.DESCRIPTION}', inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author}")
        await ctx.send(embed=embed)