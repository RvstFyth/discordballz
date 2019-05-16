'''
Manages the fighter object.

Last update: 16/05/19
'''

# Init

import asyncio

class Fighter:
    '''
    Represent a player's fighter.
    
    `client` : must be `discord.Client` object.

    `global_id` : must be type `int` and represent the fighter's global id.

    `unique_id` : must be type `str` and represent the fighter's unique id.

    `Character` : must be `Character` object.

    1. Attributes :
    
    - global_id = Return the character global id.
    - unique_id = Return the character unique id.
    - BASE_HP = Return the init HP.
    - BASE_KI_REGEN = Return the init ki regen.
    - BUFF : Return the character's buff (list of objects)
    - DEBUFF : Return the character's debuff (list of objects)
    - DOT : Return the character's DoTs (list of objects)
    - current_hp = Return the character's current hps
    - current_ki_regen = Return the character's current ki regen
    '''

    def __init__(self, client, unique_id, Character):
        self.client = client
        self.Character = Character
        self.global_id = Character.global_id
        self.unique_id = unique_id

        # Attributes
        # Basic stats, these ones shouldn't be changed.

        self.BASE_HP = None
        self.BASE_KI_REGEN = None
        
            # Effects manager
        
        self.BUFF = []  # Represent the list of benefic effects
        self.DEBUFF = []  # Represent the list of non-benefic effects
        self.DOT = []  # Represent the list of damage over time effects

        # Represent the current stats, they can be changed

        self.current_hp = self.BASE_HP  # Init at base max hp
        self.current_ki_regen = self.BASE_KI_REGEN

    # Methods

    async def base_hp(self):
        '''
        `coroutine`

        Return the character's init max HPs

        Return: int
        '''

        base_hp = await self.Character.base_hp()
        self.BASE_HP = base_hp

        return(base_hp)