'''
'''

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog
from random import randint

# Utils

from cogs.utils.functions.commands.fight.fight_system import Pve_Fight

from cogs.objects.character.characters_list.all_char import Get_char
from cogs.objects.character.characters_list.char_1 import Char_1
from cogs.objects.character.characters_list.char_2 import Char_2
from cogs.objects.character.characters_list.char_3 import Char_3

class Cmd_Fight(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx):

        # just randomly generate a team for test
        liste = []
        lenght = randint(1,3)
        char_num = 3  # represent the number of character in the game

        for generate in range(lenght):
            await asyncio.sleep(0)

            random_char = await Get_char(randint(1,char_num))

            random_char.level = randint(1,150)
            random_char.rarity_value = randint(0,5)
            random_char.type_value = randint(0,5)

            liste.append(random_char)
        
        await Pve_Fight(self.client, ctx, ctx.message.author, liste)
        
def setup(client):
    client.add_cog(Cmd_Fight(client))