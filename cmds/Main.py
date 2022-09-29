import discord, json, random
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json', 'r', encoding='utf8') as jfiles:
    jdata = json.load(jfiles)

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

    @commands.command()
    async def roll(self, ctx, rolls = 100):
        await ctx.send(f'你擲出了**{random.randrange(1,rolls)}**點')

def setup(bot):
    bot.add_cog(Main(bot))