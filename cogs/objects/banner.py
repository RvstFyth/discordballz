'''
Manages the informations about banners.

Last update: 30/06/19
'''

# dependancies

import asyncio

# object

from cogs.objects.database import Database

# utils

from cogs.objects.character.characters_list.all_char import Get_char

# config

from configuration.main_config.banner_config import REGULAR_PORTAL
from configuration.main_config.banner_config import TOTAL_CHAR_NUMBER

class Regular_banner:
    '''
    Handle the informations about the current regular banner.

    `client` : must be `discord.Client`.

    Attributes :
        name : str - Represent the banner name.
        content : list[Character] - Represent the banner content, the list contains character instances.
        image : str - Represent the banner image URL.
        cost : int - Represent the cost of a regular portal.

    Methods :
        coroutine - init() : Init the object.
        coroutine - summon(is_multi_summon : False) : Generates a random character.

    '''

    def __init__(self, client):
        self.client = client
        self.db = Database(self.client)
        self.cost = 0

        # attr
        self.name = None
        self.content = []
        self.image = None
    
    # methods

    async def init(self):
        '''
        `coroutine`

        Init the banner object.
        '''

        # queries

        name_query = 'SELECT banner_name FROM banner_regular WHERE reference = {};'.format(REGULAR_PORTAL)

        content_query = 'SELECT banner_content FROM banner_regular WHERE reference = {};'.format(REGULAR_PORTAL)

        image_query = 'SELECT banner_image FROM banner_regular WHERE reference = {};'.format(REGULAR_PORTAL)

        # exec the queries

        self.name = str(await self.db.fetchval(name_query))
        self.image = str(await self.db.fetchval(image_query))
        self.content = str(await self.db.fetchval(content_query))

        # split the content

        self.content = self.content.split()

        # now replace the content list by character instances

        character_instances = []

        for character in self.content:
            await asyncio.sleep(0)

            if(character.isdigit()):  # convert the character
                character = int(character)

                if(character != 0):
                    character = await Get_char(character)

                    character_instances.append(character)
                
                else:
                    pass
            
            else:
                pass
        
        # replace the list

        self.content = character_instances

        return
    
    # generate a random character for the summon
    async def summon(self, is_multi_summon = False):
        '''
        `coroutine`

        Generate a random character.

        If it's a multi-summon generate a list of 5 characters.

        `is_multi_summon`[Optional] : bool - If true generates a list of 5 characters. (False)

        Return: Instance of `Character` or `list`[Character()]. If not found return `None`.
        '''

        # init

        from random import randint, uniform
        from configuration.main_config.banner_config import RATE_N, RATE_R, RATE_SR, RATE_SSR

        ##

        if not is_multi_summon:  # if it's a single summon

            # init

            drawn_character = None

            n_list, r_list, sr_list, ssr_list = [], [], [], []

            for char_id in range(1, TOTAL_CHAR_NUMBER+1):  # Check all existing characters and put them into lists
                await asyncio.sleep(0)

                character = await Get_char(char_id)  # get the instance

                if(character.rarity_value == 0):  # if N
                    n_list.append(character)
                
                elif(character.rarity_value == 1):  # if R
                    r_list.append(character)
                
                elif(character.rarity_value == 2):  # if SR
                    sr_list.append(character)
                
                elif(character.rarity_value >= 3):  # if SSR or higher
                    ssr_list.append(character)
                
                else:
                    pass
            
            # draw a random character

            # SSR character

            if(len(ssr_list) > 0):  # if not empty
                draw = uniform(0, 100)
                if(draw <= RATE_SSR): # if drawn
                    drawn_character = ssr_list[randint(0, len(ssr_list)-1)]  # pick a random into the list
                
                else:
                    pass
            
            # SR character

            if(len(sr_list) > 0):
                draw = uniform(0, 100)
                if(draw <= RATE_SR):
                    drawn_character = sr_list[randint(0, len(sr_list)-1)]
                
                else:
                    pass

            # R character

            if(len(r_list) > 0):  # if not empty
                draw = uniform(0, 100)
                if(draw <= RATE_R):  # draw an R
                    drawn_character = r_list[randint(0, len(r_list)-1)]
                
                else:
                    pass

            # N character

            if(len(n_list) > 0):  # if there is at least one N character
                draw = uniform(0, 100)
                if(draw <= RATE_N):  # if draw N
                    # generate a random character in n_list
                    drawn_character = n_list[randint(0, len(n_list)-1)]
                
                else:  # else we go out
                    pass

            return(drawn_character)  # return a single Character()
        
        else:  # if multisummon
            pass
        
            return