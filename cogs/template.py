import discord, os, time, random, asyncio
from datetime import datetime
from discord.ext import commands

berhenti = False
class commands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    
    @commands.command()
    @commands.is_owner()
    async def template():
      print("test")


def setup(client):
    client.add_cog(commands(client))
    print("Loaded template.")