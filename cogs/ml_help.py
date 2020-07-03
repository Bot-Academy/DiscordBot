import discord
from discord.ext import commands
from discord.ext.commands import Paginator, Context

from bot import client


class ML_Help(commands.Cog):
    def __init__(self, client: client):
        self.client = client


def setup(client: client):
    client.add_cog(ML_Help(client))
