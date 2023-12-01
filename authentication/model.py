from peewee import Model, CharField, IntegerField, PostgresqlDatabase
# Define your PostgreSQL database connection
database = PostgresqlDatabase('postgres_db', user='postgres', password='admin123', host='localhost')

class Authenticate(database.Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = database
        
database.connect()
# database.create_tables([Authenticate])                            

# creating one row in the database
# person = Authenticate.create(name='Muhammed',age = 30)

# for fetching the all records in the database
# query = Authenticate.select()

# for all in query:
#     print(all.name,all.age)

# database.close()