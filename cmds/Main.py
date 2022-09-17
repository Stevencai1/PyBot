import imp
import discord, json
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json', 'r', encoding='utf8') as jfiles:
    jdata = json.load(jfiles)

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

def setup(bot):
    bot.add_cog(Main(bot))