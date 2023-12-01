from peewee import Model, CharField, IntegerField, PostgresqlDatabase
# Define your PostgreSQL database connection
database = PostgresqlDatabase('postgres_db', user='postgres', password='admin123', host='localhost')

class Governer(database.Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = database
        
database.connect()
# database.create_tables([Governer])                               # only one time is called , after creating database we don't want this code so comment it.

# creating one row in the database
# person = Governer.create(name='Muhammed',age = 30)

# for fetching the all records in the database
query = Governer.select()

for all in query:
    print(all.name,all.age)

database.close()

