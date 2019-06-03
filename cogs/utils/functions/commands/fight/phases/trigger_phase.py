'''
Manages the trigger phase of the fight.

Last update: 03/06/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

async def Triggers_phase(client, ctx, player, character_team, enemy_team, team_num):
    '''
    `coroutine`

    Trigger the characters effects.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    `character_team` : must be list of `Character` objects.

    `team_num` : must be type `int` : 0 = Player team, 1 = Enemy team.

    Return: discord.Message
    '''

    # Init

    _ = await Translate(client, ctx)

    # Character team

    team_display = ''
    team_effects = False
    team_triggers = ''

        # Buff
    team_buff = False
    team_buff_display = _('\n__Effects__ : ')
    team_buff_stack_display = _('\n__Stack__ : ')
    team_buff_damage_display = _('\n__Healing__ : ')
    team_buff_duration_display = _('\n__Time remaining__ : ')
    
    team_buff_total_stack = 0
    team_buff_total_duration = 0
    team_buff_total_damage = 0

        # Debuff
    team_debuff = False
    team_debuff_display = _('\n__Effects__ : ')
    team_debuff_stack_display = _('\n__Stack__ : ')
    team_debuff_damage_display = _('\n__Damages__ : ')
    team_debuff_duration_display = _('\n__Time remaining__ : ')
    
    team_debuff_total_stack = 0
    team_debuff_total_duration = 0
    team_debuff_total_damage = 0

        # Dot
    team_dot = False
    team_dot_display = _('\n__Effects__ : ') # List the character dots
    team_dot_stack_display = _('\n__Stack__ : ')
    team_dot_damage_display = _('\n__Damages__ : ')
    team_dot_duration_display = _('\n__Time remaining__ : ')

    team_dot_total_stack = 0
    team_dot_total_duration = 0
    team_dot_total_damage = 0

    # Calculating
        
    for character in character_team:
        await asyncio.sleep(0)
        
        # Effects
        # If there is any effects, we display it

        if team_effects:  # If there is already an effect, we do dot anything
            pass
        
        else:
            team_effects = False

        # Is buff effect ?

        if team_buff :
            pass
        
        else:
            team_buff = False

        # Is debuff effect ?

        if team_debuff :
            pass
        
        else:
            team_debuff = False

        # Is dot effect ?

        if team_dot:  # If there is already a dot we don't do anything
            pass
        
        else:
            team_dot = False  # If the character has active effects pass to true

        # Effects
        # Buff

        for buff in character.buff : 
            await asyncio.sleep(0)

            # Check if the effect is active
            if buff.duration <= 0:
                character.buff.remove(buff)  # The effect is, over, removing it

                if(len(character.buff) == 0):
                    break  # No more buff to check, we go out of the loop
            
            buff_damage_done = await buff.apply(character, character_team, enemy_team)  # Apply the buff's effects

            # Duration
            buff.duration -= 1

            team_effects = True
            team_buff = True

            # Set buff display

            team_buff_display += '`{}`{} | '.format(buff.name, buff.icon)
            team_buff_total_stack += buff.stack
            team_buff_total_damage += buff_damage_done
            team_buff_total_duration += buff.duration
        
        # Debuff

        for debuff in character.debuff :
            await asyncio.sleep(0)

            # Check if the effect is active or not
            if debuff.duration <= 0:
                character.debuff.remove(debuff)

                if(len(character.debuff) == 0):
                    break
            
            debuff_damage_done = await debuff.apply(character)

            # Duration
            debuff.duration -= 1

            team_effects = True
            team_debuff = True

            # Set debuff display

            team_debuff_display += '`{}`{} | '.format(debuff.name, debuff.icon)
            team_debuff_total_stack += debuff.stack
            team_debuff_total_damage += debuff_damage_done
            team_debuff_total_duration += debuff.duration

        # Dot
        for dot in character.dot :
            await asyncio.sleep(0)

            # If one of the effect is over
            if(dot.duration <= 0):
                character.dot.remove(dot)

                if(len(character.dot) == 0):  # If the character has no dot, we go out of the loop
                    break

            # If the effect is not over, apply the effect

            team_effects = True
            team_dot = True

            dot_damage_done = await dot.apply(character)

            # The character has a dot on him, we display
            
            team_dot_display += '`{}`{} | '.format(dot.name, dot.icon)
            team_dot_total_stack += dot.stack
            team_dot_total_damage += dot_damage_done
            team_dot_total_duration += dot.duration
        
        # Regens
        # Ki   

        character.current_ki += character.ki_regen  # Apply the ki regen

        if(character.current_ki > character.max_ki):  # If the ki regen is over the max, we set to max
            character.current_ki = character.max_ki
        
        # Health

        character.current_hp += character.health_regen

        if(character.current_hp > character.max_hp):
            character.current_hp = character.max_hp
    
    ### END CALCULATION ###

    # End check effects for team
    # Display

    if team_effects:
        if team_buff:

            # Buff
            team_triggers += _('------------ Buffs ------------')
            team_buff_stack_display += '{:,}'.format(team_buff_total_stack)
            team_buff_duration_display += '{:,}'.format(team_buff_total_duration)

            # Buff name
            team_triggers += team_buff_display
            # Buff stack
            team_triggers += team_buff_stack_display
            # Buff damage
            team_buff_damage_display += '**+ {:,}** :hearts:'.format(team_buff_total_damage)
            team_triggers += team_buff_damage_display
            # Buff duration
            team_triggers += team_buff_duration_display + '\n'
        
        if team_debuff:

            # Debuff
            team_triggers += _('------------ Debuffs ------------')
            team_debuff_stack_display += '{:,}'.format(team_buff_total_stack)
            team_debuff_duration_display += '{:,}'.format(team_buff_total_duration)

            # Debuff name
            team_triggers += team_debuff_display
            # Debuff stack
            team_triggers += team_debuff_stack_display
            # Debuff damage
            team_debuff_damage_display += '**{:,}**'.format(team_debuff_total_damage)
            team_triggers += team_debuff_damage_display
            # Debuff duration
            team_triggers += team_debuff_duration_display + '\n'

        if team_dot:
            
            # DOT
            team_triggers += _('------------ Damages over time ------------')
            team_dot_stack_display += '{:,}'.format(team_dot_total_stack)
            team_dot_damage_display += '**{:,}**'.format(team_dot_total_damage)
            team_dot_duration_display += '{:,}'.format(team_dot_total_duration) + _(' turns')
            
            # Dot name
            team_triggers += team_dot_display
            # Dot stack
            team_triggers += team_dot_stack_display
            # Dot damages
            team_triggers += team_dot_damage_display
            # Dot duration
            team_triggers += team_dot_duration_display + '\n'

        if(team_num == 0):
            team_display += _('\n🔵 - {}\'s Team :\n').format(player.name) + team_triggers + '\n'
        
        elif(team_num == 1):
            team_display += _('\n🔴 - Enemy Team :\n').format(player.name) + team_triggers + '\n'

        # Send
        await ctx.send(team_display)