'''
'''

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog

# Utils

from cogs.utils.functions.commands.fight.fight_system import Pve_Fight

from cogs.objects.character.characters_list.char_1 import Char_1
from cogs.objects.character.characters_list.char_2 import Char_2
from cogs.objects.character.characters_list.char_3 import Char_3

class Cmd_Fight(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx):
        
        enemy = Char_1()
        enemy.rarity_value = 5
        enemy.level = 150
        enemy.type_value = 0

        enemy_b = Char_2()
        enemy_b.rarity_value = 5
        enemy_b.type_value = 1
        enemy_b.level = 150

        enemy_c = Char_3()
        enemy_c.rarity_value = 5
        enemy_c.type_value = 2
        enemy_c.level = 150

        liste = [enemy, enemy_b, enemy_c]
        
        await Pve_Fight(self.client, ctx, ctx.message.author, liste)
        
def setup(client):
    client.add_cog(Cmd_Fight(client))