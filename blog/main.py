from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models
app = FastAPI()
db = SessionLocal()

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Person(OurBaseModel):
    id : int
    firstname : str
    lastname : str
    isMale : bool

# Function for getting records from the database as python list.
@app.get('/',response_model=list[Person],status_code=status.HTTP_200_OK)
def get_all_persons():
    get_allpersons = db.query(models.Person).all()
    return get_allpersons

#Function for inserting a record into database.
@app.post('/addperson',response_model=Person,status_code=status.HTTP_201_CREATED)
def add_Person(person:Person):
    newPerson = models.Person(
        id = person.id,
        firstname = person.firstname,
        lastname = person.lastname,
        isMale = person.isMale
    )

    find_person = db.query(models.Person).filter(models.Person.id == person.id).first()

    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="User with this id is already exists.")
    db.add(newPerson)
    db.commit()

    return newPerson


# Function for Updating the record in the  database
@app.put('/update_person/{person_id}',response_model=Person,status_code= status.HTTP_202_ACCEPTED)

def Update_record(person_id:int,person:Person):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if find_person is not None:
        find_person.id = person_id
        find_person.firstname = person.firstname
        find_person.lastname = person.lastname
        find_person.isMale = person.isMale

        db.commit()
        return find_person
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No user with the provided user id")



#Function for delete a record from the database
@app.delete('/delete_person/{person_id}')
def delete_person(person_id : int):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if find_person is not None:
        db.delete(find_person)
        db.commit()
        return find_person
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="user with the provided user id is either deleted or not found")


































































































# @app.get('/')
# async def create():
#     return {'Message':'server is running'}
# @app.get('/getthepersonbyid/{person_id}')
# async def get_person_id(person_id:int):
#     return {"Message":f"Your Person_id is {person_id}"}

# @app.post('/addthepersoninfo')
# def add_person_details(person: Person):
#     return {
#          'id' : person.id,
#         'firstname': person.firstname,
#         'lastname' : person.lastname,
#         'isMale' : person.isMale
#     }




