'''
This is the dummy, test everything you want on it.

Last update: 27/05/19
'''

# Dependancies

from cogs.objects.enemy import Enemy

class Dummy(Enemy):
    '''
    Represents : `Dummy`
    '''

    # Instance attributes

    def __init__(self):
        # Basic infos
        self.name = 'Dummy'
        self.image = 'https://i.imgur.com/qNzaU4B.png'  # Image URL
        self.category = 0
        self.type = 0
        self.rarity = 0

        # Fight infos
        self.max_hp = 5000
        self.current_hp = self.max_hp
        self.max_ki = 100
        self.current_ki = self.max_ki
        self.damage_max = 500
        self.damage_min = int(90*(self.damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.defense = 0
        self.critical_chance = 0 # In %
        self.dodge_chance = 0  # In %
        self.ki_regen = 0
        self.health_regen = 0

        # Abilities infos
        self.ability_count = 0  # Represents the number of abilities a character has
        self.first_ability_name = ''
        self.first_ability_description = ''

        self.second_ability_name = ''
        self.second_ability_description = ''

        self.third_ability_name = ''
        self.third_ability_description = ''

        self.fourth_ability_name = ''
        self.fourth_ability_description = ''

        # Methods

    async def init(self, client, ctx):
        pass
    
    # Abilities

    async def first_ability(self):
        pass
    
    async def second_ability(self):
        pass
    
    async def third_ability(self):
        pass
    
    async def fourth_ability(self):
        pass