import discord, json, os
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
    channel = bot.get_channel(int(jdata['general_channel']))
    await channel.send(f'{member} Join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['general_channel']))
    await channel.send(f'{member} Leave!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Load {extension} completed!')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unload {extension} completed!')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reload {extension} completed!')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['token'])