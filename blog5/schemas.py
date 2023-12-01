from peewee import Model, PostgresqlDatabase

database = PostgresqlDatabase('postgres_db', user='postgres', password='admin123', host='localhost', port=5432)

from peewee import CharField, Model

class NewTable(Model):
    filename = CharField()
    filepath = CharField()

    class Meta:
        database = database
        
# database.connect()
# try:
#     database.create_tables([NewTable])
#     print("table created successfully")
# except:
#     print("Some error occured")