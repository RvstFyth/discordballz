'''
Manages the effect of the Acid dot.

Last update: 08/06/19
'''

# Dependancies
import asyncio

# classes
from cogs.objects.class_referencer import Get_class
from cogs.objects.character.abilities_effects.damages_over_time._dot_object import Dot

# Utils

from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_buff, Get_dot
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_buff, Has_dot
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
        self.initial_duration = 4
        self.duration = 4

        # Stacks
        self.max_stack = 3
        self.stack = 1

        # Damages
        self.total_damage = 0
        self.tick_damage = 0

        # Method const
        self.saibaiman_id = [1,2,3]  # represents the ids of the saibaimans
    
    # Method

    async def init(self, client, ctx):
        '''
        `coroutine`

        Translate the names.
        '''

        _ = await Translate(client, ctx)

        self.name = _('Acid')

        return
    
    async def set_total_damage(self, caster, target, team_a, team_b):
        '''
        `coroutine`

        Set the total damage based on the saibaiman with the highest amount of ki in the team_a

        and the target max hp.

        Return: int (total damage)
        '''

        highest_ki = caster.ki_damage_max

        for saibaiman in team_a:
            await asyncio.sleep(0)

            if(saibaiman.id in self.saibaiman_id):  # if its a saibaiman
                if(saibaiman.ki_damage_max > highest_ki):
                    highest_ki = saibaiman.ki_damage_max
            
            else:
                pass

        self.total_damage = int(((1+((highest_ki/1000)*0.5))*target.max_hp)/100) 

        return(self.total_damage)
    
    async def set_tick_damage(self, caster, target, team_a, team_b):
        '''
        `coroutine`

        Set the Acid total damage and tick damage

        Return: int (tick damage)
        '''

        self.caster = caster

        self.tick_damage = int((self.total_damage/self.initial_duration)*self.stack)

        return(self.tick_damage)

    async def add_stack(self, caster, target, team_a, team_b):
        '''
        `coroutine`

        Adds a stack of acid to the target. The damages are based on the Saibaiman with the highest

        amount of ki_damage_max in the team_a (ally team).

        Also reset the initial duration of Acid and re-calculate the tick damage based on the new stack.

        Add 2 stacks if at least one ally has Unity is strenght.
        '''
        self.caster = caster
        # init
        highest_ki = caster.ki_damage_max  # get the char with the highest amount of ki damage
        unity = False  # false if any character in the ally team has the Unity is strenght effect

        # classes
        acid_ = await Get_class(1)
        unity_ = await Get_class(2)

        acid_, unity_ = acid_(), unity_()

        # define the highest amount of damage
        for ally in team_a:
            await asyncio.sleep(0)

            if ally.id in self.saibaiman_id:  # if the ally is a saibaiman
                if(ally.ki_damage_max > highest_ki):
                    highest_ki = ally.ki_damage_max
                
                else:
                    pass
            
            else:  # not a saibaiman
                pass
        
        # find someone in the ally team with the unity buff

        for character in team_a:
            await asyncio.sleep(0)

            has_unity = await Has_buff(character, unity_)

            if has_unity:  # if the character has unity we can break because we have found at least one character with the buff
                unity = True
                break
            
            else:
                pass
        
        # now we can increase the stacks

        has_acid = await Has_dot(target, acid_)

        if has_acid:  # if the target has the Acid dot active on it
            acid_ = await Get_dot(target, acid_)  # get the dot instance

            # now increase the stack if the limit hasn't been reached
            if(acid_.stack < acid_.max_stack):
                if unity:  # if at least one character in the team has unity is strenght
                    acid_.stack += 2
                    acid_.duration = acid_.initial_duration  # reset the duration

                    if(acid_.stack > acid_.max_stack):  # if we over the limit
                        acid_.stack = acid_.max_stack
                
                else:  # if any character in the caster team has the buff unity is strenght
                    acid_.stack += 1
                    acid_.duration = acid_.initial_duration

            else:  # if the stack limit has been reached
                acid_.duration = acid_.initial_duration  # just reset the duration
            
            # Re-calculate the tick damages

            acid_.tick_damage = await acid_.set_tick_damage(caster, target, team_a, team_b)

        else:  # if the target doesn't have acid
            if unity:
                acid_.stack = 2
                acid_.initial_duration = 5

                acid_.total_damage = await acid_.set_total_damage(caster, target, team_a, team_b)
                acid_.tick_damage = await acid_.set_tick_damage(caster, target, team_a, team_b)
            
            else:
                acid_.stack = 1
                
                acid_.total_damage = await acid_.set_total_damage(caster, target, team_a, team_b)
                acid_.tick_damage = await acid_.set_tick_damage(caster, target, team_a, team_b)
            
            target.dot.append(acid_)

        return

    async def apply(self, client, ctx, target, team_a, team_b):
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

                await target.inflict_damage(client, ctx, self.caster, damage_done, team_a, team_b)
            
            else:
                damage_done = self.tick_damage  # Ignores the defense

                await target.inflict_damage(client, ctx, self.caster, damage_done, team_a, team_b)
        
        return(damage_done)