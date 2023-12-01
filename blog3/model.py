import peewee
from peewee import Model, CharField, IntegerField, PostgresqlDatabase
# Define your PostgreSQL database connection
database = PostgresqlDatabase('postgres_db', user='postgres', password='admin123', host='localhost')

class Files_Uploader(database.Model):
    filename = CharField()
    discription = str

    class Meta:
        database = database
        
database.connect()
try:
    database.create_tables([Files_Uploader]) 
    print("Database named Files_Uploader created successfully")
except:
    print("Some error is occured.")










































































# only one time is called , after creating database we don't want this code so comment it.

# creating one row in the database
person = Governer.create(name='Muhammed',age = 30)

for fetching the all records in the database
query = Governer.select()

for all in query:
    print(all.name,all.age)

database.close()


