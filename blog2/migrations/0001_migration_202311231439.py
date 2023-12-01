# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Governer(peewee.Model):
    name = CharField(max_length=255)
    age = IntegerField()
    class Meta:
        table_name = "governer"


