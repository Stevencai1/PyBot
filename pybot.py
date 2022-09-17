import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is Online!")

@bot.event
async def on_member_join(member):
    print(f'{member} Joined!')

bot.run("ODUzMTgxMDI2MzQwMDQ0ODAx.GSWrNt.-csLOzEW1O0CWmuXqVMEllfOiLqjtD7oIQsLBY")