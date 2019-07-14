"""
Manages the translation of the program.

--

Author : DrLarck

Last update : 14/07/19
"""

# dependancies
import asyncio, gettext

# utils
from utility.database.database_manager import Database

# translator
class Translator:
    """
    Allow the translation of the strings.

    - Parameter : 
    
    `db_pool` : Represents a connection pool to the database. Initially stored in `client.db`.

    `player` : Represents a :class:`Player()`. Basically the caller of the string that will be translated.

    - Attribute : 

    `language` : Represent the `player` language. The :class:`Translator()` will translate all the strings to that language.

    - Method :
    """

    # attribute 
    def __init__(self, db_pool, player):
        # parameters
        self.db = Database(db_pool)
        self.player = player

        # init
        self.language = None
        self.translator = None
    
    # method   
        # init
    async def get_language(self):
        """
        `coroutine`

        Get the player's lang to set up the translation language.

        --

        Return : Language initials (i.e ISO 639-1 Code), `None` if not found.
        """

        # init
        self.language = await self.db.fetchval(f"SELECT player_lang FROM player_info WHERE player_id = {self.player.id};")

        self.language = self.language.upper()

        # returns the ISO 639-1 code of the language
        return(self.language)
    
        # translation
    async def translate(self):
        """
        `coroutine`

        Returns the tools needed to allow us translate the strings based on the caller language.

        To translate a string, do :

        `_(f"String to {word}")`

        --

        Return : gettext.gettext as `_()`
        """

        # init
        await self.get_language()

        if(self.language == "FR"):
            # get the directory of the translation
            # and set up the translation
            fr_translation = gettext.translation("fr", localedir = "locale", languages = ["fr"])
            fr_translation.install()

            # translate the string 
            self.translator = fr_translation.gettext

        else:
            # if None language has been found, return the english string
            gettext.install("locale/dbz_translation")

            self.translator = gettext.gettext

        return(self.translator)