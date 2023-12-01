import peewee
from fastapi import FastAPI,Query,Path,Body,UploadFile,File,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from model import database,Files_Uploader
app = FastAPI()

# Functin for uploading a file into a database(postgres) table.


@app.post("/file_upload")
async def file_upload(file: UploadFile=File(...)):
    with database.atomic():
        uploaded_file = Files_Uploader.create(filename = file.filename)
    return {"filename": file.filename, "file_id": uploaded_file.id}
        
    

# Function for fetch the files



@app.post("/get_records")
async def get_records(filename : str=Query(..., description="The filename to retrieve")):
    try:
        file_record = Files_Uploader.get(Files_Uploader.filename == filename)
    except Files_Uploader.DoesNotExist:
        raise HTTPException(status_code=404,detail="File is not found")
    return {"filename":file_record.filename}




""" if you want to save a file with it's path may be from your system or from aws storage or other"""

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), filepath: str = "/path/to/files/"):
    # Save file information to the database
    with database.atomic():
        uploaded_file = Files_Uploader.create(filename=file.filename, filepath=filepath + file.filename)

    return {"filename": file.filename, "file_id": uploaded_file.id, "filepath": uploaded_file.filepath}