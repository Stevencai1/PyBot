import discord, json, random
from discord.ext import commands
with open('setting.json', 'r', encoding='utf8') as jfiles:
    jdata = json.load(jfiles)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is Online!")

@bot.event
async def on_member_join(member):
    print(f'{member} Join!')
    channel = bot.get_channel(int(jdata['general_channel']))
    await channel.send(f'{member} Join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} Leave!')
    channel = bot.get_channel(int(jdata['general_channel']))
    await channel.send(f'{member} Leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run(jdata['token'])