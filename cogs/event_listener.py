import discord
from discord.ext import commands


class Event_Listener(commands.Cog):

    def init(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[Status] Ready")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("> Command does not exist")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("> Please add all required arguments")

        elif isinstance(error, commands.BotMissingAnyRole):
            await ctx.send("> You do not have permmission to use this command")

        await ctx.send(error)


def setup(client):
    client.add_cog(Event_Listener(client))
