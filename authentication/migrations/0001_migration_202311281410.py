# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Authenticate(peewee.Model):
    username = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    class Meta:
        table_name = "authenticate"


