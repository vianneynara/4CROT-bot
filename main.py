import disnake
import json
import os
import dotenv
import time
from disnake.ext import commands

intents = disnake.Intents.all()
disnake.member = True
bot = commands.Bot(command_prefix='>', intents=intents, case_insensitive=True, help_command=None)


with open("settings.json") as file:
    settings = json.load(file)


@bot.event
async def on_ready():
    print("=====================")
    print("Bot Online")
    print("====================")

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.channel)
async def ping(ctx):
    await ctx.reply(f"🏓 Pong! ``{round(bot.latency * 1000)} ms``")

@bot.event
async def on_member_join(member):
    print(f"{member} joined the server ")

@bot.event
async def on_member_remove(member):
    print(f"{member} left the server")

@bot.command()
async def load(ctx, extension):
    if ctx.author.guild_permissions.administrator:
        bot.load_extension(f'cogs.{extension}')
        await ctx.reply(f'loaded {extension}')

@bot.command()
async def unload(ctx, extension):
    if ctx.author.guild_permissions.administrator:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.reply(f'unloaded {extension}')

@bot.command(name="reload", aliases=["refresh"])
async def reload(ctx, extension):
    if ctx.author.guild_permissions.administrator:
        extension = extension.lower()
        bot.unload_extension(f'cogs.{extension}')
        time.sleep(1)
        bot.load_extension(f'cogs.{extension}')
        await ctx.reply(f'Reloaded {extension}')


@bot.command(name='shutdown')
async def shutdown(ctx):
    print(ctx.author, "initiated shutdown.")
    if ctx.author.id in [389034898666553344]:
        exit()
    else:
        return
    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@reload.error
async def reload_error(self, ctx, error):
    ctx.reply("Lu mau refresh yang mana goblok")
    
bot.run(os.environ.get("TOKEN"))
