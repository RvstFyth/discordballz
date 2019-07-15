"""
Manages the selection phase.

--

Author : DrLarck

Last update : 13/07/19
"""

# dependancies
import asyncio

# utils
    # translation
from utility.translation.translator import Translator

    # displayer
from utility.cog.displayer.character import Character_displayer

# selection phase manager
class Selection_phase:
    """
    Manages the selection phase.

    - Parameter :

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self, client, ctx, player, turn):
        self.client = client
        self.player = player
        self.ctx = ctx
        self.turn = turn

    # method
    async def start_selection(self, team):
        """
        `coroutine`

        Start the selection phase.

        --

        Return : None
        """

        # init
        translation = Translator(self.client.db, self.player)
        #_ = await translation.translate()
        move = []  # stores the move in it.
        order = 1  # display the character's order number

        for character in team:
            await asyncio.sleep(0)

            if(character.health["current"] > 0 and character.posture["stunned"] == False):
                # displying the character
                displayer = Character_displayer(self.client, self.ctx, self.player)
                displayer.character.append(character)

                await displayer.display(combat_format = True)
                await asyncio.sleep(2)

                # displaying the kit
                if(self.turn == 1):  # first turn
                    kit = "`1. Skip the turn ⏩`"
                    kit += "`3. Defend 🏰`\n"
        
                else:
                    kit = "`1. Sequence 👊` |"
                    kit += "`2. Ki charge 🔥` |"
                    kit += "`3. Defend 🏰`"
                    kit += "\n\n__Abilities__ :\n\n"

        return