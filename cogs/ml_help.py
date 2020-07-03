import discord
from discord.ext import commands
from discord.ext.commands import Paginator, Context

from bot import client


class ML_Help():
    def __init__(self, client: client):
        self.client = client

    @commands.Command()
    async def mlhelp(self, ctx: Context):
        pass


def setup(client: client):
    client.add_cog(ML_Help(client))
