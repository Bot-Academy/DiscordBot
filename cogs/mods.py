import discord
from discord.ext import commands
from discord.ext.commands import Context

from bot import client


class Mods(commands.Cog):

    def __init__(self, client: client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Owner")
    async def clear(self, ctx: Context, amount=10):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_any_role("Owner")
    async def kick(self, ctx: Context, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_any_role("Owner")
    async def ban(self, ctx: Context, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_any_role("Owner")
    async def unban(self, ctx: Context, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {member_name}#{member_discriminator}')
                return


def setup(client: client):
    client.add_cog(Mods(client))
