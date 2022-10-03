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
        rolls_value = random.randrange(-10,rolls)
        await ctx.send(f'你擲出了**{rolls_value}**點')
        if rolls_value >= 90:
            await ctx.send(f'**大吉**')
        elif rolls_value < 90 and rolls_value > 10:
            await ctx.send(f'中吉')
        elif rolls_value <= 10 and rolls_value >=0:
            await ctx.send(f'*小吉*')
        else:
            await ctx.send(f'~~*兇*~~')
        if rolls_value == 100 or rolls_value == -10:
            await ctx.send(f'__**高雄發大財**__')

def setup(bot):
    bot.add_cog(Main(bot))