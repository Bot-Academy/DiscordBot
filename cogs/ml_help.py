import discord
from discord.ext import commands
from discord.ext.commands import Paginator, Context

from bot import client


class ML_Help(commands.Cog):
    def __init__(self, client: client):
        self.client = client

    @commands.command()
    async def test(self, ctx: Context):
        paginator = commands.Paginator()
        paginator.add_line('some line')
        paginator.add_line('some other line')
        for page in paginator.pages:
            await ctx.send(page)


def setup(client: client):
    client.add_cog(ML_Help(client))
