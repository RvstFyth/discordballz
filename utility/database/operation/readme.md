# Database operation

## Tips
### Create a table

To create a table, do not type your SQL query manually. Use the `Table_creator` object.

Simply create your own `function` and add it to the `Table_creator().tables` attribute. Then run the `create_all()` method or directly create your table using `create_table()` without using `.tables`.