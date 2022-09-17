import discord, json
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json', 'r', encoding='utf8') as jfiles:
    jdata = json.load(jfiles)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['general_channel']))
        await channel.send(f'<@{member.id}> 加入了伺服器！')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['general_channel']))
        await channel.send(f'<@{member.id}> 離開了伺服器！')

    @commands.Cog.listener()
    async def on_message(self, msg):
        sleep = ['ZZZ', 'zzz']
        if msg.content in sleep and msg.author != self.bot.user:
            await msg.channel.send('ZZZzzz')

def setup(bot):
    bot.add_cog(Event(bot))