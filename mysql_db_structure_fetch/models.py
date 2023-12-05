# In this directory we will connect our database and fetch the structure of database such as tables and respective columns.

import mysql.connector
import pandas as pd
import json
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mysql"
)



# Fetch tables
cursor = connection.cursor()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()


# Fetch table structures
table_structures = {}
for table in tables:
    table_name = table[0]
    cursor.execute(f"DESCRIBE {table_name};")
    columns = cursor.fetchall()
    table_structures[table_name] = [column[0] for column in columns]

json_format = json.dumps(table_structures,indent=2)
print(json_format)

# getting table schema as json format




# getting table records as json format
# sql_query = 'SELECT * FROM hello2'
# # read the data using pandas
# df = pd.read_sql(sql_query,connection)

# # convert this dataframe into json format

# json_data = df.to_json(orient="records")
# print(json_data)




# geting table schema as json format

# cursor = connection.cursor(dictionary=True)
# sql_query = "DESCRIBE hello2"

# # Execute SQL Query and Fetch Schema
# cursor.execute(sql_query)
# table_schema = cursor.fetchall()

# schema_json = json.dumps(table_schema, indent=2)
# print(schema_json)











































