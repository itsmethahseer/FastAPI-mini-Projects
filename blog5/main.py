from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
from schemas import database, NewTable
import magic
from uuid import uuid4
import boto3
from loguru import logger
from datetime import datetime


kb = 1024
mb = 1024 * kb

SUPPORTED_FILE_TYPES = {
    "image/png": "png",
    "image/jpeg": "jpeg",
    "application/pdf": "pdf",
}

aws_access_key_id = "replace your was access key"
aws_secret_access_key = "replace with your was secret key"
region_name = "replace with your region"

AWS_BUCKET = "myawsbucket1234567890100"
s3 = boto3.resource(  # Use boto3.resource instead of boto3.client
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)
bucket = s3.Bucket(AWS_BUCKET)

# Function for uploading filename into both table and file into uploads directory.

# @app.post("/upload-file/")
# async def create_upload_file(file: UploadFile = File(...)):
#     try:
#         # Save file to database
#         with database.atomic():
#             file_model = NewTable.create(
#                 filename=file.filename, filepath=str(Path("uploads") / file.filename)
#             )
#             file_model.save()

#         # Save file to directory
#         with open(str(Path("uploads") / file.filename), "wb") as file_object:
#             shutil.copyfileobj(file.file, file_object)

#         return JSONResponse(content={"message": "File uploaded successfully"})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# function for uploading a file into aws s3 bucket
async def s3_upload(contents: bytes, key: str):
    logger.info(f"Uploading {key} to S3")
    bucket.put_object(Key=key, Body=contents)


app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file found!"
        )

    contents = await file.read()
    size = len(contents)

    if not 0 < size <= 1 * mb:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please provide a file size less than 1 MB!",
        )

    file_type = magic.from_buffer(buffer=contents, mime=True)
    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type: {file_type}, supported types are {SUPPORTED_FILE_TYPES}",
        )

    await s3_upload(
        contents=contents, key=f"{uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}"
    )
    return JSONResponse(content={"message": "File uploaded successfully"})
