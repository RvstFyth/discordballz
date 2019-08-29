"""
Allows the player to manage his team

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# command
class Cmd_fighter(commands.Cog):
    
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Cmd_fighter(client))