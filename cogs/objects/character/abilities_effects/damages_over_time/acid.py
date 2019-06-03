'''
Manages the effect of the Acid dot.

Last update: 02/06/19
'''

# Dependancies

from cogs.objects.character.abilities_effects.damages_over_time.dot_object import Dot

class Acid(Dot):
    '''
    Ignore the defense of the target.
    '''

    # Class attribute

    name = 'Acid'
    id = 1
    icon = '<:acid:583953112406949888>'
    
    # Instance attributes

    def __init__(self):
        Dot.__init__(self)
        # Duration
        self.duration = 4

        # Stacks
        self.max_stack = 3
        self.stack = 0

        # Damages
        self.total_damage = 0
        self.tick_damage = 0
    
    # Method

    async def apply(self, target):
        '''
        `coroutine`

        `target` : must be `Character` object.

        Return: damages (int)
        '''

        if(self.duration > 0):
            # Dealing damages

            if(self.stack >= 3):
                damage_done = int(self.tick_damage * 1.5)  # If there is more than 3 stacks the damages are increased by 50 %
                target.current_hp -= damage_done
            
            else:
                damage_done = self.tick_damage  # Ignores the defense
                target.current_hp -= damage_done
        
        return(damage_done)