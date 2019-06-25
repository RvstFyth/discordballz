'''
Manages the ability object.

Last update: 24/06/19
'''

# Dependnancies 

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

class Ability:
    '''
    This is an ability.

    Attributes :
        Informations :
        - name : str
        - description : str
        - icon : discord.Emoji
        - id : int

        Basics :
        - cost : int
        - cooldown : int

        Target:
        - need_target : bool
        - can_target_ally : bool


    Methods :
    - coro init(self, database, ctx) :
        • Init the ability (translate the name, description etc.) : `database` : `Database` object ; ctx : `discord.ext.commands.Context` object.
    
    - coro trigger(self, client, ctx, caster, target, team_a, team_b, move) :
        • Triggers the ability : `client` : must be `discord.Client` object ; `ctx` : must be `discord.ext.commands.Context` object ;
          `caster` : must be `Character` object and represent the caster ; `target` : must be `Character` object ;
          `team_a` and `team_b` : must be `list of Character` objects ; `move` : must be `str`.
    '''
    
    icon = ''
    id = 0

    def __init__(self):
        # Informations
        self.name = ''
        self.description = ''

        # Basics
        self.cost = 0
        self.cooldown = 0

        # Target
        self.need_target = False
        self.can_target_ally = False
        self.can_target_enemy = False

    # Method

    async def init(self, client, ctx, caster):
        pass
    
    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        pass