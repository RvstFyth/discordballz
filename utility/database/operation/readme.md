# Database operation

## Tips
### Create a table

To create a table, do not type your SQL query manually. Use the `Table_creator` object.

Simply create your own `function` and add it to the `Table_creator().tables` attribute.

*Example* :
```python
# in Table_creator() or anywhere else.
# Here we're in it
# Just think to send your function to the `Table_creator().tables` attribute.
# We're going to create the table named "_test"
async def create_test(self):
    """
    Return table dict
    """

    test_table = await self.get_creation_pattern()  # return a dict pattern to create your table

    test_table["name"] = "_test"
    test_table["need_ref"] = Fasle  # Use or not a default sequence as reference for the rows
    
    # defining the attributes
    user_name = {
        "name" : "user_name",
        "type" : "text",
        "default" : None
    }

    user_age = {
        "name" : "user_age",
        "type" : "integer",
        "default" : 0
    }

    # add the attribute to the table info
    test_table["attribute"] = [
        user_name, user_age
    ]

    return(test_table)
```