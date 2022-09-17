import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print("Bot is Online!")

@bot.event
async def on_member_join(member):
    print(f'{member} Join!')
    channel = bot.get_channel(853181663964954667)
    await channel.send(f'{member} Join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} Leave!')
    channel = bot.get_channel(853181663964954667)
    await channel.send(f'{member} Leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run("ODUzMTgxMDI2MzQwMDQ0ODAx.GSWrNt.-csLOzEW1O0CWmuXqVMEllfOiLqjtD7oIQsLBY")