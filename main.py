from fastapi import FastAPI,Query,Path,Body,UploadFile,File
from pydantic import BaseModel,Field
from typing import Optional
app = FastAPI()

# @app.get("/")
# def index():
#     return {"data": {"name": "Muhammed Thahseer"}}
# @app.get("/about/unpublished")
# def unpublished():
#     return "all blogs are unpublished"
# @app.get("/about/{id}")
# def about(id:int):
#     return {"name":id}

# class Blog(BaseModel):
#     title:str
#     body:str
#     published: Optional[bool] = None
# @app.post('/request/')
# async def create_blog(request:Blog):
#     return {"data":f"blog is created with title as {request.title}"}


# class Blog(BaseModel):
#     name : str
#     discription : str | None = None
#     price : float
#     tax : float | None = None
    


# @app.post('/')
# async def fun(blog:Blog):
#     item_dict = blog.dict()
#     if blog.tax:
#         price_with_tax = blog.price + blog.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

# String Validation , using this Query class we can decide how many length character maximum we can allocate.
# @app.post('/items_validation/')
# async def read_data(q:str | None = Query(None,min_length=3,max_length=10)):
#     results = {"Message":[{"item_id":"Foo"},{"Item_id":"Foo"}]}
#     if q:
#         results.update({"q":q})
#     return results


# @app.post('/items_validation/{item_id}')
# async def read_data(item_id:int, q:str | None = Query(None,alias="Item_id ")):
#     results = {"Item_id":item_id}
#     if q:
#         results.update({"q":q})
#     return results




# # we can give the path of the output instead of output.
# @app.post('/items_validation/{item_id}')
# async def read_data(item_id:int = Path(...,title="ID of the item to get"), q:str | None = Query(None,alias="Item_id ")):
#     results = {"Item_id":item_id}
#     if q:
#         results.update({"q":q})
#     return results





# Numeric Validation , using this Query class we can decide how many size Number maximum we can allocate also minimum. I assigned the query value as hello
# so no need to add it at UI.

# @app.post('/items_validation/{item_id}')
# async def read_data(item_id:int =Path(...,ge=10,le=100) ,q:str ="Hello"):
#     results = {"item_id":item_id}
#     if q:
#         results.update({"q":q})
#     return results



# Multiple parameters

# class Item(BaseModel):
#     name : str
#     discription : str | None = None
#     price : float | None = None
#     tax : float 
    
    
# class User(BaseModel):
#     user_name : str
#     full_name : str | None = None
    
# @app.post('/items/{item_id}')
# async def update_item(*,item_id : int, q:str,item:Item , user:User ):
#     result = {"Item_id":item_id}
    
#     if q:
#         result.update({"q":q})
#     if item: 
#         result.update({"item":item})
    
#     # if user:
#     #     result.update({"User details":user})
    
#     return result

 ## HOW to use field in fastapi   
# class Item(BaseModel):
#     name : str
#     discription : str | None = Field(None,title = "Discription of the item",max_length = 300)
#     price : float = Field(...,title="Price must be greater than zero", gt=0)
#     tax : float | None = None

# @app.put('/items/{item_id}')
# async def update_item(item_id : int,item: Item = Body(...,embed=True)):
#     results =  {"Item_id":item_id,"item":item}
    
#     return results




# class Item(BaseModel):
#     name : str
#     discription : str | None = None
#     price : float
#     tax : float | None = None
#     tags : list = []
    
# @app.put('/items/{item_id}')
# async def update_item(item_id : int,item: Item = Body(...,embed=True)):
#     results =  {"Item_id":item_id,"item":item}
    
#     return results





# Uploading files into fastapi columns 


    
# @app.post('/upload_file')
# async def Hello(item : UploadFile=File(...)):
#     return {"filename": item.filename,"content":item.content_type,"filesize":item.size}

























































































