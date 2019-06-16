'''
Manages the effect of the Acid dot.

Last update: 08/06/19
'''

# Dependancies

from cogs.objects.character.abilities_effects.damages_over_time._dot_object import Dot

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

class Acid(Dot):
    '''
    Ignore the defense of the target.
    '''

    # Class attribute

    id = 1
    icon = '<:acid:583953112406949888>'
    
    # Instance attributes

    def __init__(self):
        Dot.__init__(self)
        # Info
        self.name = 'Acid'
        self.caster = None  # Represent the character who has launched this effect
        # Duration
        self.duration = 4

        # Stacks
        self.max_stack = 3
        self.stack = 1

        # Damages
        self.total_damage = 0
        self.tick_damage = 0
    
    # Method

    async def init(self, client, ctx):
        '''
        `coroutine`

        Translate the names.
        '''

        _ = await Translate(client, ctx)

        self.name = _('Acid')

        return

    async def apply(self, target, team_a, team_b):
        '''
        `coroutine`

        `target` : must be `Character` object.

        Return: damages (int)
        '''

        damage_done = 0

        if(self.duration > 0):
            # Dealing damages

            if(self.stack >= 3):
                damage_done = int(self.tick_damage * 1.5)  # If there is more than 3 stacks the damages are increased by 50 %

                await target.inflict_damage(self.caster, damage_done, team_a, team_b)
            
            else:
                damage_done = self.tick_damage  # Ignores the defense

                await target.inflict_damage(self.caster, damage_done, team_a, team_b)
        
        return(damage_done)