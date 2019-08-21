# Database operation

## Tips
### Create a table

To create a table, do not type your SQL query manually. Use the `Table_creator` object.

Simply create your own `function` and add it to the `Table_creator().tables` list attribute. Then run the `create_all()` method or directly create your table using `create_table()` without using `.tables`.

Here's a quick example :

To define a table attribute you'll need to do as following : 
```python
creator = Table_creator(self.client)
table = await creator.get_creation_pattern()
table["name"] = "my_table_name"

my_attribute = {
  "name" : "my_attribute_name",
  "type" : "text",
  "default" : "im_the_attribute"
 }
 
 table["attribute"] = [
  my_attribute
 ]
 
 return(table)  # your fonction should always return your table if you're using the .create_all() method
 ```
 Your query will be generated like this by the `.create_table()` method :
 ```sql
 CREATE TABLE IF NOT EXISTS my_table_name(
  my_attribute_name text default 'im_the_attribute'
 );
 ```
 To declare an integer :
 ```python
 my_int = {
  "name" : "my_int",
  "type" : "integer",
  "default" : 0
 }
 ```
 It will return :
 ```sql
 CREATE TABLE IF NOT EXISTS my_table_name(
  my_int integer default 0
 );
 ```
 This tool has been designed to create huge table and improve the readability of the query (and reduce the use of SQL).
 
 It's 100 % python, and usefull if you have many constrains to add.
