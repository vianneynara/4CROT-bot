import disnake
import os
import random
import time
from disnake.ext import commands
from disnake.utils import get

ripbozo = [
    "https://tenor.com/view/rip-bozo-ripus-bozus-nik0321-unlive2774-potato-chip-smoker-bozo-gif-21079712",
    "https://tenor.com/view/rip-gif-21571424",
    "https://tenor.com/view/ripbozo-lebron-rip-plug-piss-gif-20478223",
    "https://tenor.com/view/twice-laughing-laugh-nayeon-tzuyu-gif-21686501",
    "https://tenor.com/view/bigboss-metalgearsol-snake-venomsnake-rip-gif-22244218",
]


class Gif(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:

            if "forgor" in message.content.lower():
                await message.add_reaction("💀")

            elif message.content.lower().startswith(">sange sama kartun"):
                await message.reply(
                    "https://cdn.discordapp.com/attachments/880509666482860042/884722248303403008/video0-18.mp4",
                    mention_author=False,
                )

            elif "ok and?" in message.content.lower():
                await message.reply(
                    "https://tenor.com/view/file-size-was-too-big-to-upload-on-gamebanana-gif-22787008"
                )

            # elif 'rip bozo' in message.content.lower():

            # await message.reply(random.choice(ripbozo))

            # elif 'ripbozo' in message.content.lower():

            # await message.reply(random.choice(ripbozo))

            """elif "waktu berhenti" in message.content.lower():
              if message.author.id == 662839403806195729:
                await message.channel.set_permissions(get(message.guild.roles, id = 955471627448107098), send_messages=False)
            elif "waktu berjalan kembali" in message.content.lower():
              if message.author.id == 662839403806195729:
                await message.channel.set_permissions(get(message.guild.roles, id = 955471627448107098), send_messages=True)"""

    @commands.command(name="pagi")
    async def pagi(self, ctx):
        await ctx.reply(
            "https://media.discordapp.net/attachments/880509666482860042/886026262169145384/caption.gif",
            mention_author=False,
        )

    @commands.command(name="siang")
    async def siang(self, ctx):
        await ctx.reply(
            "https://media.discordapp.net/attachments/873613113855991828/878972885660733492/caption.gif",
            mention_author=False,
        )

    @commands.command(name="sore")
    async def sore(self, ctx):
        await ctx.reply(
            "https://media.discordapp.net/attachments/799121511470202921/905371859988668426/caption.gif",
            mention_author=False,
        )

    @commands.command(name="malam")
    async def malam(self, ctx):
        await ctx.reply(
            "https://media.discordapp.net/attachments/873613113855991828/878972799417466940/caption.gif",
            mention_author=False,
        )


def setup(client):
    client.add_cog(Gif(client))
    print("Loaded gif.")
