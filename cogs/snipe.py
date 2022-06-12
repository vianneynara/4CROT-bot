import disnake
from disnake.ext import commands


class Snipe(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self.bot.sniped_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        self.bot.sniped_messages[ctx.channel.id] = (
            ctx.content,
            ctx.author,
            ctx.channel.name,
            ctx.created_at,
        )

    @commands.command(name="snipe")
    @commands.cooldown(1, 20, commands.BucketType.channel)
    async def snipe(self, ctx):
        content, author, channel_name, time = self.bot.sniped_messages[ctx.channel.id]

        snipeEmbed = disnake.Embed(
            description=f"***Sniped |*** {content}",
            color=disnake.Color.red(),
            timestamp=time,
        )
        snipeEmbed.set_footer(text=f"by {author}", icon_url=author.avatar.url)

        await ctx.channel.send(embed=snipeEmbed)


def setup(client):
    client.add_cog(Snipe(client))
    print("Loaded snipe.")
