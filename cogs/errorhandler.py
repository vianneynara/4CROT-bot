import disnake
from disnake.ext import commands

import traceback
import asyncio


class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('❔')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Perintah tidak lengkap!", mention_author=False)

        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("Anda tidak bisa menggunakan itu perintah ini!")

        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.reply("Member tidak ada di server.", mention_author=False)

        # cooldown detection
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction('<:command_cooldown:960940883501547540>')
            await ctx.author.send(
                f"<@{ctx.author.id}>, tunggu ``{error.retry_after:.0f}s`` sebelum menulis perintah lain!")

        # detail error
        else:
            formatted = "".join(traceback.format_exception(type(error), error, error.__traceback__))
            print(formatted)


def setup(client):
    client.add_cog(ErrorHandler(client))
    print("Loaded errorhandler.")