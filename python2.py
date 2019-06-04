import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time







@client.event
async def on_ready():
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    client.loop.create_task(status_task())
    
    
@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Well, You've made it")
    
    
    
client.run(os.getenv('TOKEN'))
