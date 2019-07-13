"""
Manages the player hourly.

Last update : 12/07/19
"""

# dependancies

import asyncio
from time import time

# object

from cogs.objects.database import Database

class Hourly:
    """
    Get the player hourly informations and edit them.

    - Parameters :
    `client` : Represent the `commands.Bot`.

    `player` : Represents the :class:`Player`.

    - Methods :
    :coro:`get_hourly()` : Return the informations about the last player hourly.

    :coro:`get_combo()` : Return the player's combo.

    :coro:`update_hourly(value)` : Update the player's hourly info with the passed value as parameter. The value must be in `seconds`.

    :coro:`update_combo(value)` : Update the player's combo value with the passed value as parameter.
    """

    def __init__(self, client, player):
        self.client = client
        self.player = player
        self.db = Database(self.client)
    
    # methods

    async def get_hourly(self):
        """
        `coroutine`

        Get the last player's hourly.

        --

        Return: int (last hourly in sec), if not found return `None`.
        """

        # init

        last_hourly = None

        # queries
        
        get_hourly = f"SELECT player_hourly FROM player_hourly WHERE player_id = {self.player.id};"

        last_hourly = await self.db.fetchval(get_hourly)

        return(last_hourly)
    
    async def time_remaining(self):
        """
        `coroutine`

        Return a formatted string that announce the time remaining before the next hr.

        --

        Return : formatted str else return `None`
        """

        # init 
        time_remaining = None
        now = time()
        last_hourly = await self.get_hourly()

        elapsed_time = int(now - last_hourly)

        print(f"elapsed : {now} - {last_hourly}\n= {elapsed_time}")
        
        _time = 3600 - elapsed_time
        
        hour_remaining = int(_time/3600)
        _time -= hour_remaining
        print(_time)

        minute_remaining = _time/60
        _time -= minute_remaining
        print(_time)

        second_remaining = _time
        print(_time)

        hour_remaining, minute_remaining, second_remaining = int(hour_remaining), int(minute_remaining), int(second_remaining)

        time_remaining = f"{hour_remaining}h : {minute_remaining}m : {second_remaining}s"

        return(time_remaining)
    
    async def get_combo(self):
        """
        `coroutine`

        Get the player's hourly combo.

        --

        Return : int (combo value), if not found return `None`.
        """

        # init

        combo = None

        # queries

        get_combo = f"SELECT player_hourly_combo FROM player_hourly WHERE player_id = {self.player.id};"

        combo = await self.db.fetchval(get_combo)

        return(combo)
    
    async def update_hourly(self, value):
        """
        `coroutine`

        Update the player hourly value.

        `value` : Represent the new `time` value in seconds.
        """

        # queries

        update_hourly = f"UPDATE player_hourly SET player_hourly = {value} WHERE player_id = {self.player.id};"

        await self.db.execute(update_hourly)

        return
    
    async def update_combo(self, value):
        """
        `coroutine`

        Update the combo value.

        `value` : Represent the new combo value.
        """

        # queries

        update_combo = f"UPDATE player_hourly SET player_hourly_combo = {value} WHERE player_id = {self.player.id};"

        await self.db.execute(update_combo)

        return