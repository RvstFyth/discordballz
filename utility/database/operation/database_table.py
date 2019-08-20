"""
Table creation

-- 

Author : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
import asyncio
from utility.database.database_manager import Database

# table creator
class Table_creator:
    """
    Create the needed tables.

    - Parameter :

    `client` : Represents a `discord.Client`. This client must handle a database pool (i.e Database().init())
    """

    # attribute
    def __init__(self, client):
        self.db = Database(client.db)
        self.tables = [
            self.create_player_info
        ]
    
    # method
    async def create_all(self):
        """
        `coroutine`

        Create all the tables.

        --

        Return : None
        """

        # trigger all the function stored in creation
        for func in self.tables:
            await asyncio.sleep(0)

            # get table info
            table_info = await func()

            # create the table with the infos
            await self.create_table(
                table_info["name"],
                table_info["attribute"],
                need_ref = table_info["need_ref"],
                unique_index = table_info["unique_index"]
            )
        
        return
    
    async def get_creation_pattern(self):
        """
        `coroutine`

        Returns a table creation pattern for `create_table()`.

        --

        Return : dict

        - Key

        table_pattern :

        `name` : str - The table name.
 
        `unique_index` : list - A list of unique index needed. Default None.

        `attribute` : list - A list of attribute for the table.

        `need_ref` : bool - Default false.

        attribute pattern :

        `name` : str - The row name.

        `type` : srt - The row type.

        `default` : depend - Tells if the row admits a default value. If not None, set the value of the 
        default key as the default value for the row.
        """

        # init
        table_pattern = {
            "name" : None,
            "unique_index" : None,
            "need_ref" : False,
            "attribute" : None
        }

        return(table_pattern)
    
    async def create_table(self, name, attribute, need_ref = False, unique_index = None):
        """
        `coroutine`

        Tool that allows you to create a table easily according to the creation pattern returned by
        `get_creation_pattern()`.

        - Parameter :

        `name` : The table name. Lower Case.

        `attribute` : A list of dictionnary of the table attribute. Obtained using `get_creation_pattern()`.

        `need_ref` : Default `False`. Set a sequence or not for the table.

        `unique_index` : A list of unique index to create (name of rows to constrain).

        --

        Return : None
        """

        # init
        query = ""
        index = 0

        # set up the query for the creation
        if(need_ref):  # the table needs a reference
            query += f"CREATE SEQUENCE IF NOT EXISTS {name}_reference_seq;\n"
                
            # table creation
        query += f"CREATE TABLE IF NOT EXISTS {name}(\n" 
        if(need_ref):  # add the sequence into the query
            query += f"\treference BIGINT PRIMARY KEY DEFAULT nextval('{name}_reference_seq') NOT NULL,\n"
        
        # add the attributes
        for attr in attribute:
            await asyncio.sleep(0)

            # add the attribute line
            query += f"\t{attr['name']} {attr['type']}"

            if(attr['default'] != None):  # if the attr has a default value
                if(type(attr['default']) == str):
                    query += f" DEFAULT '{attr['default']}'"

                else:
                    query += f" DEFAULT {attr['default']}"

            # check if there is no more attribute
            index += 1
            if(index < len(attribute)):  # there is other attribute
                query += ",\n"
            
            else:  # there is no more attribute
                query += "\n);\n"
        
        # unique reference index
        if(need_ref):
            query += f"CREATE UNIQUE INDEX IF NOT EXISTS {name}_ref_index ON {name}(reference);\n"
        
        # check the unique index
        if(unique_index != None):
            query += f"CREATE UNIQUE INDEX IF NOT EXISTS {name}_index ON {name}("

            index = 0
            for row in unique_index:
                await asyncio.sleep(0)

                query += row

                index += 1
                if(index < len(unique_index)):  # there is other row
                    query += ", "
                
                else:  # no more row to add
                    query += ");"
        
        await self.db.execute(query)

        return
    
    # tables
        # player
    async def create_player_info(self):
        """
        `coroutine`

        Creates the table player_info.

        --

        Return : dict i.e self.get_creation_pattern
        """

        # init
        player_info = await self.get_creation_pattern()

        player_info["name"] = "player_info"
        player_info["need_ref"] = True

        # attribute
        player_id = {
            "name" : "player_id",
            "type" : "BIGINT",
            "default" : None
        }

        player_name = {
            "name" : "player_name",
            "type" : "TEXT",
            "default" : None
        }

        player_register_date = {
            "name" : "player_register_date",
            "type" : "TEXT",
            "default" : None
        }

        player_lang = {
            "name" : "player_lang",
            "type" : "TEXT",
            "default" : "EN"
        }

        player_location = {
            "name" : "player_location",
            "type" : "TEXT",
            "default" : "UNKNOWN"
        }

            # add the attribute
        player_info["attribute"] = [
            player_id, player_name, player_register_date, player_lang, player_location
        ]

        # unique index
        player_info["unique_index"] = [
            player_id["name"]
        ]

        return(player_info)