from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()
""" Uploading a file using fastapi to create api's"""


# @app.post("/files")
# async def add_files(file:Annotated[bytes | None ,File()]=None):
#     if file is None:
#         return {"Message":"File is not added."}
#     return {"file-size":len(file)}

# @app.post("/upload_files")
# async def upload_files(file: UploadFile|None = None):
#     if not file:
#         return {"File is not added, please add the file"}
#     return {"file is added sucessfully"}




""" To upload multiple files """

@app.post("/upload_files")
async def multiple_uploads(file: list[UploadFile]):
    return {"following files are uploaded successully ":[files.filename for files in file]}


    