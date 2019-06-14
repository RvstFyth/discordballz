'''
'''

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Cog

# Utils

from cogs.utils.functions.commands.fight.fight_system import Pve_Fight

from cogs.objects.character.characters_list.char_1 import Char_1

class Cmd_Fight(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx):
        
        enemy = Char_1()
        enemy.rarity_value = 0
        enemy.level = 20
        enemy.type_value = 0

        enemy_b = Char_1()
        enemy_b.rarity_value = 1
        enemy_b.type_value = 1
        enemy_b.level = 40

        enemy_c = Char_1()
        enemy_c.rarity_value = 2 
        enemy_c.type_value = 2
        enemy_c.level = 60

        enemy_d = Char_1()
        enemy_d.rarity_value = 3
        enemy_d.type_value = 3
        enemy_d.level = 80

        enemy_e = Char_1()
        enemy_e.rarity_value = 4
        enemy_e.type_value = 4
        enemy_e.level = 120

        liste = [enemy, enemy_b, enemy_c, enemy_d, enemy_e]
        
        await Pve_Fight(self.client, ctx, ctx.message.author, liste)
        
def setup(client):
    client.add_cog(Cmd_Fight(client))