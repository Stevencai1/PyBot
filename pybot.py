import discord, json, os, asyncio
from discord.ext import commands
with open('setting.json', 'r', encoding='utf8') as jfiles:
    jdata = json.load(jfiles)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is Online!")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Load `{extension}` completed!')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unload `{extension}` completed!')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reload `{extension}` completed!')

async def main():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')
    await bot.start(jdata['token'])

if __name__ == "__main__":
    asyncio.run(main())