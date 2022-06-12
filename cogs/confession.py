import disnake
from disnake.ext import commands
import datetime


class Confession(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(name="confess")
    @commands.dm_only()
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def confess(self, ctx, tipe, *, message: str):
        print(ctx.author.name + "#" + ctx.author.discriminator + ": " + message)
        # mengirim confession
        if tipe not in ("anon", "anonim", "publik", "public"):
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(
                "Kamu harus memilih tipe confession yang benar! (anon/publik)"
            )

        if message is None:
            return await ctx.reply("Kamu harus memasukan sebuah pesan/confession!")

        # mengirim sesuai permintaan tipe confession
        if tipe in ("anon", "anonim"):
            confession = disnake.Embed(
                title="Confession", description=message, color=0xFFFFFF
            )
            confession.set_footer(text="❔ Anonim")
            confession.timestamp = datetime.datetime.utcnow()
            await ctx.bot.get_channel(958714095580897350).send(embed=confession)
            await ctx.bot.get_channel(958744662523408464).send(
                f"`{ctx.author.name}#{ctx.author.discriminator}`/<@{ctx.author.id}> confessed: {message}"
            )
            return await ctx.reply("Confession telah dikirim ke <#958714095580897350>!")
        elif tipe in ("publik", "public"):
            pengirim = str(ctx.author.name + "#" + ctx.author.discriminator)
            confession = disnake.Embed(
                title="Confession", description=message, color=0xFFFFFF
            )
            confession.set_footer(text=pengirim, icon_url=ctx.author.avatar.url)
            confession.timestamp = datetime.datetime.utcnow()
            await ctx.bot.get_channel(958714095580897350).send(embed=confession)
            await ctx.bot.get_channel(958744662523408464).send(
                f"`{ctx.author.name}#{ctx.author.discriminator}`/<@{ctx.author.id}> confessed: {message}"
            )
            return await ctx.reply("Confession telah dikirim ke <#958714095580897350>!")


def setup(client):
    client.add_cog(Confession(client))
    print("Loaded confession.")
