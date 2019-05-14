'''
Manages the way the units are summonned by players.

Last update: 14/05/19
'''

# Dependancies

import asyncio
from random import uniform, randint

# Rates

from configuration.main_config.droprate_config import LR_CATEGORY_RATE, SCOUTER_CATEGORY_RATE, OUT_SCOUTER_CATEGORY_RATE
from configuration.main_config.droprate_config import SCOUTER_SSR_RATE, SCOUTER_SR_RATE, OUT_SCOUTER_N_RATE, OUT_SCOUTER_R_RATE, OUT_SCOUTER_SR_RATE, OUT_SCOUTER_SSR_RATE

# Database
    # Portal

from cogs.utils.functions.database.select.portal.regular_portal import Select_regular_portal_infos
from cogs.utils.functions.database.select.character.character import Select_character_infos

async def Summoner(client, portal):
    '''
    `coroutine`

    Manages the drop rates of the units and how they are summonned.

    `client` : must be `discord.Client` object.

    `portal` : must be type `int` and represent the portal the player is summonning with.

    Return: int (char global id)
    '''

    # Init

    portal = await Select_regular_portal_infos(client, portal)
    char_returned = None

    # Now we get the legendary characters

    legendary = portal['legendary']
    legendary = legendary.split()  # Change it to an array, now we can exploit it

    # Now we get the scouter characters

    scouter = portal['scouter']
    scouter = scouter.split()
    
    # Now we set the out-of-scouter one

    out_scouter = portal['out of scouter']
    out_scouter = out_scouter.split()

    # Now category test
        # Lr category test

    if not legendary[0] == 'NONE':

        category_test = uniform(0, 100)  # Draw a random number
        if(category_test <= LR_CATEGORY_RATE):
            # Now the player has obtained an access to the LR characters
            # We randomly pick a legendary character

            char_returned = legendary[randint(0, len(legendary)-1)]

            return(int(char_returned))
    
        # Scouter category test

    if not scouter[0] == 'NONE':

        category_test = uniform(0,100)
        if(category_test <= SCOUTER_CATEGORY_RATE):
            # Now we test the rarity
            # and return a random character in the category 

            scouter_ssr, scouter_sr = [], []

            # Now we just add the split the characters in function of their rarity
            
            for a in range(len(scouter)):
                # Init

                await asyncio.sleep(0)  # Asynchronous

                character = await Select_character_infos(client, int(scouter[a]))  # We get the information of the character stored at the scouter[a] pos

                # Now we add the characters in the lists

                if(character['rarity'].upper() == 'SSR'):
                    scouter_ssr.append(int(scouter[a]))
                
                elif(character['rarity'].upper() == 'SR'):
                    scouter_sr.append(int(scouter[a]))
                
                else:
                    pass

            rarity_test = uniform(0, 100)
            if(rarity_test <= SCOUTER_SSR_RATE):
                # len-1 because we start at 0
                char_returned = scouter_ssr[randint(0, len(scouter_ssr)-1)]

                return(int(char_returned))
            
            rarity_test = uniform(0, 100)
            if(rarity_test <= SCOUTER_SR_RATE):

                char_returned = scouter_sr[randint(0, len(scouter_sr)-1)]

                return(int(char_returned))
    
        # Out of scouter category test
    
    if not out_scouter[0] == 'NONE':

        out_scouter_ssr, out_scouter_sr, out_scouter_r, out_scouter_n = [], [], [], []

        # Split the out of scouter characters into the lists

        for b in range(len(out_scouter)):
            # Init

            await asyncio.sleep(0)

            character = await Select_character_infos(client, int(out_scouter[b]))

            if(character['rarity'].upper() == 'SSR'):
                out_scouter_ssr.append(int(out_scouter[b]))
            
            elif(character['rarity'].upper() == 'SR'):
                out_scouter_sr.append(int(out_scouter[b]))
            
            elif(character['rarity'].upper() == 'R'):
                out_scouter_r.append(int(out_scouter[b]))
            
            elif(character['rarity'].upper() == 'N'):
                out_scouter_n.append(int(out_scouter[b]))
            
            else:
                pass
        
        category_test = uniform(0, 100)
        if(category_test <= OUT_SCOUTER_CATEGORY_RATE):

            rarity_test = uniform(0, 100)
            if(rarity_test <= OUT_SCOUTER_SSR_RATE):

                char_returned = out_scouter_ssr[randint(0, len(out_scouter_ssr)-1)]

                return(int(char_returned))
            
            rarity_test = uniform(0, 100)
            if(rarity_test <= OUT_SCOUTER_SR_RATE):

                char_returned = out_scouter_sr[randint(0, len(out_scouter_sr)-1)]

                return(int(char_returned))
            
            rarity_test = uniform(0, 100)
            if(rarity_test <= OUT_SCOUTER_R_RATE):

                char_returned = out_scouter_r[randint(0, len(out_scouter_r)-1)]

                return(int(char_returned))
            
            rarity_test = uniform(0, 100)
            if(rarity_test <= OUT_SCOUTER_N_RATE):

                char_returned = out_scouter_n[randint(0, len(out_scouter_n)-1)]

                return(int(char_returned))
    
    else:
        return('NONE')