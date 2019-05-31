'''
Manages how the damages are calculated.

Last update: 31/05/19
'''

# Dependancies 

import asyncio
from random import randint

# Utils

from cogs.utils.functions.commands.fight.functions.type_advantage import Is_type_advantaged

async def Damage_calculator(fighter, target, is_sequence = False, is_ki = False, ignore_defense = False):
    '''
    `coroutine`

    Calculates the damage a unit does in function of the parameters.

    `fighter` : must be `Fighter` object.

    `target` : must be `Character` object.

    `is_sequence` : must be type `bool` default `False`, pass True if its a sequence attack.

    `is_ki` : must be type `bool` default set to `False` and tells if the incoming damages are from a ki ability or not.

    `ignore_defense` : must be type `bool` default set to `False`

    Return: int (damage value)
    '''

    # Init 

    '''
    G (% damage Modification) = 1+%.
    For reduced damage you have 1 + (-%) as it is a (-) modification
    For increased damage you have 1  + (%) as it is a (+) modification
    If the character takes 20% reduced damage G= .8,
    If the character takes 20% increased damage G= 1.2
    This portion was fixed, i had the numbers backwards (G)

    T (Type advantage bonus) = TypeAdv + (Bonus/100).
    TypeAdv = 0.8 if disadvantage, 1.2 if advantaged
    Bonus = From abilities.  If the ability deals 10% bonus type advantage damage then it is ((+10)/100), if the ability deals 10% reduced type advantage damage then it is ((-10)/100)

    Crit = 1 if not crit, (1.5 + (critbonus / 100)) if cri

    Remove : R, F, D, B, M, V
    Damage = ((Damages x B) + D) x T x G x V x ((2500 + M) / ((2500 + (Defense - F)) x R))) x Crit

    New : (Damages[from Variance (90 % to 100 %)])*T*G*(2,500 / (2,500 + Defense))*Crit
    '''

    # Init

    calculated_damages = 0
    
    # Type 

    type_advantage = await Is_type_advantaged(fighter, target)

    if type_advantage == 0:
        # If there is nothing
        type_advantage = 1
    
    elif type_advantage == 1:
        type_advantage = 1.2

    else:
        type_advantage = 0.8
     
    # Damages

    fighter_damage = randint(fighter.stat.damage_min, fighter.stat.damage_max)

    if is_sequence:
        fighter_damage = fighter_damage*0.8
    
    else:
        pass

    damage_reduction = 1+(fighter.stat.damage_reduction) 

    # Defense

    phy_defense, ki_defense = 2500/(2500 + target.stat.physical_defense), 2500/(2500 + target.stat.ki_defense)
    
    # Critical roll

    roll = randint(0, 100)
    if(roll <= fighter.stat.critical_chance):
        critical_bonus = 1.5 + (fighter.stat.critical_bonus)/100
    
    else:
        critical_bonus = 1

    if not ignore_defense:  # If the defense is not ignored
        if not is_ki:
            print(fighter_damage, type_advantage, damage_reduction, phy_defense, critical_bonus)
            calculated_damages = (fighter_damage)*type_advantage*damage_reduction*phy_defense*critical_bonus
        
        else:  # If KI ability
            calculated_damages = (fighter_damage)*type_advantage*damage_reduction*ki_defense*critical_bonus
    
    else:  # If ignore defense
        calculated_damages = (fighter_damage)*type_advantage*damage_reduction*critical_bonus

    return(int(calculated_damages))