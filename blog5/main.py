from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
from schemas import database,NewTable


app = FastAPI()

# Function for uploading filename into both table and file into uploads directory.

@app.post("/upload-file/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        # Save file to database
        with database.atomic():
            file_model = NewTable.create(
                filename=file.filename, filepath=str(Path("uploads") / file.filename)
            )
            file_model.save()

        # Save file to directory
        with open(str(Path("uploads") / file.filename), "wb") as file_object:
            shutil.copyfileobj(file.file, file_object)

        return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
