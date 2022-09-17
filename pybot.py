import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

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

bot.run("ODUzMTgxMDI2MzQwMDQ0ODAx.GSWrNt.-csLOzEW1O0CWmuXqVMEllfOiLqjtD7oIQsLBY")