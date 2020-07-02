import discord
from discord.ext import commands
from discord.ext.commands import Paginator, Context


class ML_Help():
    def __init__(self, client):
        self.client = client

    @commands.Command()
    async def mlhelp(self, ctx: Context):
        pass


def setup(client):
    client.add_cog(ML_Help(client))
