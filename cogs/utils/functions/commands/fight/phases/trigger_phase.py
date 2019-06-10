'''
Manages the trigger phase of the fight.

Last update: 10/06/19
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

    character_count = 1

    # Character team
    team_effects = False
    char_effect = False
    team_triggers = ''
        
    # Calculating
        
    for character in character_team:
        await asyncio.sleep(0)
        
        # Reinit
        character_trigger = ''

        # Buff
        team_buff = False
        team_buff_display = _('\n__Effects__ : ')
        team_buff_stack_display = _('\n__Stack__ : ')
        team_buff_damage_display = _('\n__Healing__ : ')
        team_buff_duration_display = _('\n__Time remaining__ : ')
        
        # Debuff
        team_debuff = False
        team_debuff_display = _('\n__Effects__ : ')
        team_debuff_stack_display = _('\n__Stack__ : ')
        team_debuff_damage_display = _('\n__Damages__ : ')
        team_debuff_duration_display = _('\n__Time remaining__ : ')
        
        # Dot
        team_dot = False
        team_dot_display = _('\n__Effects__ : ') # List the character dots
        team_dot_stack_display = _('\n__Stack__ : ')
        team_dot_damage_display = _('\n__Damages__ : ')
        team_dot_duration_display = _('\n__Time remaining__ : ')
        
        # Passives

        if character.has_leader:
            await character.Leader_skill(character, character_team, enemy_team)

        if character.has_passive:
            await character.Passive_skill(character, character_team, enemy_team)
            
        # Effects
        # If there is any effects, we display it
        
        char_effect = False

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
            
            else:
                buff_damage_done = await buff.apply(character, character_team, enemy_team)  # Apply the buff's effects

                # Duration
                buff.duration -= 1

                team_effects = True
                char_effect = True
                team_buff = True

                # Set buff display
                team_buff_display += '`{}`{} | '.format(buff.name, buff.icon)
                team_buff_stack_display += '**{}** | '.format(buff.stack)
                team_buff_damage_display += '+ **{}**:hearts: | '.format(buff_damage_done)
                team_buff_duration_display += '**{}** | '.format(buff.duration)
        
        if(team_buff):  # If the character has a buff we display it
            character_trigger += _('\n------------ Buffs ------------')
            character_trigger += team_buff_display
            character_trigger += team_buff_stack_display
            character_trigger += team_buff_damage_display
            character_trigger += team_buff_duration_display
            character_trigger += '\n'
        
        # Debuff

        for debuff in character.debuff :
            await asyncio.sleep(0)

            # Check if the effect is active or not
            if debuff.duration <= 0:
                character.debuff.remove(debuff)

                if(len(character.debuff) == 0):
                    break
            
            else:
                debuff_damage_done = await debuff.apply(character)

                # Duration
                debuff.duration -= 1

                team_effects = True
                char_effect = True
                team_debuff = True

                # Set debuff display
                team_debuff_display += '`{}`{} | '.format(debuff.name, debuff.icon)
                team_debuff_stack_display += '**{}** | '.format(debuff.stack)
                team_debuff_damage_display += '- **{}** | '.format(debuff_damage_done)
                team_debuff_duration_display += '**{}** | '.format(debuff.duration)
        
        if(team_debuff):  # If character has a debuff we display it
            character_trigger += _('\n------------ Debuffs ------------')
            character_trigger += team_debuff_display
            character_trigger += team_debuff_stack_display
            character_trigger += team_debuff_damage_display
            character_trigger += team_debuff_duration_display
            character_trigger += '\n'

        # Dot
        for dot in character.dot :
            await asyncio.sleep(0)

            # If one of the effect is over
            if(dot.duration <= 0):
                character.dot.remove(dot)

                if(len(character.dot) == 0):  # If the character has no dot, we go out of the loop
                    break
            
            else:
            
                # Duration
                dot_damage_done = await dot.apply(character)
                dot.duration -= 1

                # If the effect is not over, apply the effect

                team_effects = True
                char_effect = True
                team_dot = True

                # The character has a dot on him, we display
                team_dot_display += '`{}`{} | '.format(dot.name, dot.icon)
                team_dot_stack_display += '**{}** | '.format(dot.stack)
                team_dot_damage_display += '- **{}** | '.format(dot_damage_done)
                team_dot_duration_display += '**{}** | '.format(dot.duration)
        
        if(team_dot):  # if character has a dot we display it
            character_trigger += _('\n------------ Damages over time ------------')
            character_trigger += team_dot_display
            character_trigger += team_dot_stack_display
            character_trigger += team_dot_damage_display
            character_trigger += team_dot_duration_display
            character_trigger += '\n'
        
        # Regens
        # Ki   

        character.current_ki += character.ki_regen  # Apply the ki regen

        if(character.current_ki > character.max_ki):  # If the ki regen is over the max, we set to max
            character.current_ki = character.max_ki
        
        # Health

        character.current_hp += character.health_regen

        if(character.current_hp > character.max_hp):
            character.current_hp = character.max_hp
        
        # Display character name

        if(char_effect):
            team_triggers += '\n#{} - **{}**{}{} :{}'.format(character_count, character.name, character.rarity_icon, character.type_icon, character_trigger)

        character_count += 1

    ### END CALCULATION ###

    # End check effects for team
    # Display

    if team_effects:
        if(team_num == 0):
            final_display = _('🔵 - {}\'s Team :').format(player.name) + team_triggers + '\n'
        
        elif(team_num == 1):
            final_display = _('\n\n🔴 - Enemy Team :').format(player.name) + team_triggers + '\n'

        # Send
        await ctx.send(final_display)