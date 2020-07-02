import discord
from discord.ext import commands
from discord.ext.commands import Context


class Event_Listener(commands.Cog):

    def init(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[Status] Ready")

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error):
        embed = discord.Embed()

        embed.add_field(name="**Error**", value=("> " + str(error)))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Event_Listener(client))
