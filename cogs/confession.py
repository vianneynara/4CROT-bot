import disnake
from disnake.ext import commands
import datetime


class confession(commands.Cog):
    def __init__(self, client):
        self.bot = client
  
    @commands.command(name="confess")
    @commands.dm_only()
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def confess(self, ctx, type, *, message:str):
        print(ctx.author.name + "#" + ctx.author.discriminator + ": " + message)
        # mengirim confession
        if message is None:
            await ctx.reply("Kamu harus memasukan sebuah pesan/confession!")
            
        # mengirim sesuai permintaan tipe confession
        if type in ("anon", "anonim"):
            confession = disnake.Embed(title="Confession", description=message, color=0xFFFFFF)
            confession.set_footer(text="❔ Anonim")
            confession.timestamp = datetime.datetime.utcnow()
            await ctx.bot.get_channel(958714095580897350).send(embed=confession)
            await ctx.bot.get_channel(958744662523408464).send(f"`{ctx.author.name}#{ctx.author.discriminator}`/<@{ctx.author.id}> confessed: {message}")
            await ctx.reply("Confession telah dikirim ke <#958714095580897350>!")
        elif type in ("publik", "public"):
            pengirim = str(ctx.author.name + "#" + ctx.author.discriminator)
            confession = disnake.Embed(title="Confession", description=message, color=0xFFFFFF)
            confession.set_footer(text=pengirim, icon_url=ctx.author.avatar.url)
            confession.timestamp = datetime.datetime.utcnow()
            await ctx.bot.get_channel(958714095580897350).send(embed=confession)
            await ctx.bot.get_channel(958744662523408464).send(f"`{ctx.author.name}#{ctx.author.discriminator}`/<@{ctx.author.id}> confessed: {message}")
            await ctx.reply("Confession telah dikirim ke <#958714095580897350>!")


def setup(client):
    client.add_cog(confession(client))
    print("Loaded confession.")