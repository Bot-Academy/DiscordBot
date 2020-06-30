import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.')


@client.command()
@commands.has_role("Owner")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded Cog")


@client.command()
@commands.has_role("Owner")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloaded Cog")


@client.command()
@commands.has_role("Owner")
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded Cog")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[0:-3]}')

client.run('NzIyNzI1NjYwOTQ2MzMzNzA2.XvkS4g.pMtZGIGBE1lPUNRHwZIwMg-8qcs')
