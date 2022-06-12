import disnake
import os
import time
import dotenv
import datetime
import pytz
from disnake.ext import commands

intents = disnake.Intents.all()
disnake.member = True
bot = commands.Bot(
    command_prefix=">",
    intents=intents,
    case_insensitive=True,
    help_command=None
)

dotenv.load_dotenv()
dt = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))


@bot.event
async def on_ready():
    print("=====================")
    print("Bot Online")
    print("====================")
    await bot.get_channel(int(os.environ.get("STARTCH"))).send(
        f"> :green_circle: **Operational** | <t:{int(dt.timestamp())}:F> | {dt.strftime('%d/%m/%Y')}, {dt.strftime('%H:%M:%S')} *(Asia/Jakarta)*"
    )


@bot.command()
@commands.cooldown(1, 15, commands.BucketType.channel)
async def ping(ctx):
    await ctx.reply(f"🏓 Pong! ``{round(bot.latency * 1000)} ms``")


@bot.command()
async def load(ctx, extension):
    if ctx.author.guild_permissions.administrator:
        bot.load_extension(f"cogs.{extension}")
        await ctx.reply(f"loaded {extension}")


@bot.command()
async def unload(ctx, extension):
    if ctx.author.guild_permissions.administrator:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.reply(f"unloaded {extension}")


@bot.command(name="reload", aliases=["refresh"])
async def reload(ctx, extension):
    if ctx.author.guild_permissions.administrator:
        extension = extension.lower()
        bot.unload_extension(f"cogs.{extension}")
        time.sleep(1)
        bot.load_extension(f"cogs.{extension}")
        await ctx.reply(f"Reloaded {extension}")


@bot.command(name="shutdown")
async def shutdown(ctx):
    print(ctx.author, "initiated shutdown.")
    if ctx.author.id in [389034898666553344]:
        exit()
    else:
        return


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@reload.error
async def reload_error(ctx, error):
    ctx.reply(f"Lu mau refresh yang mana goblok ({error.__context__})")


print("Bot is starting up...")
bot.run(os.environ.get("TOKEN"))
