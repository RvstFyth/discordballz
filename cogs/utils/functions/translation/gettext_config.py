'''
Manages the translation language.

Last update: 08/05/19
'''

# Dependancies

import gettext, asyncio, time

# Database

from cogs.utils.functions.database.select.player.player import Select_player_language
async def Translate(client, ctx):
    '''
    Translate an `str` object passed to the `_()` as parameter.

    To format the passed string please do as following : `_('A string to format {}').format(x)`.

    Return: str
    '''

    # Init

    player = ctx.message.author
    player_language = await Select_player_language(client, player)

    if(type(player_language) == str):
        player_language = player_language.upper()
    
    else:
        return
    
    # French translation

    if(player_language == 'FR'):
        french_translation = gettext.translation('fr', localedir = 'locale', languages = ['fr'])
        french_translation.install()

        _ = french_translation.gettext

        return(_)
    
    else:
        gettext.install('locale/discordballz_translation')

        _ = gettext.gettext

        return(_)