import discord
from discord.ext import commands
from discord.ext.commands import Context
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = commands.Bot(command_prefix='.')


@client.command()
@commands.has_role("Owner")
async def load(ctx: Context, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded Cog")


@client.command()
@commands.has_role("Owner")
async def unload(ctx: Context, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloaded Cog")


@client.command()
@commands.has_role("Owner")
async def reload(ctx: Context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded Cog")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[0:-3]}')

client.run(BOT_TOKEN)
