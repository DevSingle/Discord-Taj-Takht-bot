import asyncio
import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents, help_command=None, case_insensitive=True)
    
loaded_extensions = {}

for path, subdirs, files in os.walk('cogs/'):
    for name in files:
        if name.endswith('.py'):
            filename = os.path.join(path, name).replace('/', '.').replace('\\', '.')[:-3]
            cog_name = name[:-3].split('.')[-1]
            loaded_extensions[cog_name] = filename
            bot.load_extension(filename)
bot.loaded_extensions = loaded_extensions

async def status_task():
    while True:
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="👑 Server"))
        await asyncio.sleep(35)
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="You :)"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="🧶 /info"))
        await asyncio.sleep(40)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    # bot.loop.create_task(status_task())
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="🧶|Coming Soon..."))


@bot.event
async def on_command_error(ctx: nextcord.Message, error: Exception):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
        title="دسترسی غیره مجاز 🤷‍♂️",
        description="شما به این کامند دسترسی ندارید!😁",
        color=nextcord.Color.red()
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_footer(text="Coming Soon")
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(
        title="دسترسی غیره مجاز 🤷‍♂️",
        description="شما به این کامند دسترسی ندارید!😁",
        color=nextcord.Color.red()
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_footer(text="Coming Soon")
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        pass
    else:
        pass



@bot.command()
@commands.is_owner()
async def ping(ctx):
    latency = bot.latency
    await ctx.reply(f'Pong! Latency: {latency * 1000:.2f}ms')


bot.run(os.getenv('TOKEN'))
