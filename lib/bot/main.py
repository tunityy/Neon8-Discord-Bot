import discord
import sqlite3
from discord.ext import commands
from discord.ext.commands import command, has_permissions, bot_has_permissions
from glob import glob


owners = [148311502716141568]
COGS = [path.split('\\')[-1][:-3] for path in glob('./lib/cogs/*.py')]
client = commands.Bot(case_insensitive=True, command_prefix = '.', owner_ids=set(owners)) # intents=intents)  or maybe intents=Intents.all())? #TODO: look up intents in the docs


### EVENTS ###

@client.event
async def on_ready():
    print(f"\nI'm combat ready!\n")
    await client.get_channel(823615456605896754).send("Reporting for duty!")

@client.event
async def on_connect():
    print('Connection established.\n')

@client.event
async def on_disconnect():
    print('Bot disconnected.')


### COMMANDS ###

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!  |  {round(client.latency * 1000)}ms")


### COGS ###

@client.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'lib.cogs.{extension}')
    await ctx.send(f"Cog {extension} loaded")

@client.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'lib.cogs.{extension}')
    await ctx.send(f"Cog {extension} unloaded")

@client.command()
@has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'lib.cogs.{extension}')
    client.load_extension(f'lib.cogs.{extension}')
    await ctx.send(f"Cog {extension} reloaded")

for cog in COGS:
    client.load_extension(f'lib.cogs.{cog}')
    print(f'{cog} cog loaded')


### RUN ###

with open('./lib/bot/token.0', 'r', encoding='utf-8') as tf:
    TOKEN = tf.read()

client.run(TOKEN)