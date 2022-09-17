import discord, json
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json', 'r', encoding='utf8') as jfiles:
    jdata = json.load(jfiles)

class React(Cog_Extension):
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'已成功清除 `{num}` 個訊息！')

def setup(bot):
    bot.add_cog(React(bot))