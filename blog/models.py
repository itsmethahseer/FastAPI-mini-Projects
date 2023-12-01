from sqlalchemy import Column,Integer,String,Boolean
from database import Base,engine

def create_tables():
    Base.metadata.create_all(engine)

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    isMale = Column(Boolean)







