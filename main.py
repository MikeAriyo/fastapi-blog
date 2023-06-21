from typing import Optional
from fastapi import FastAPI  #importing
from pydantic import BaseModel


app = FastAPI(); #creating an instance of fastapi

@app.get('/blog')  #(/) base path

#path operator function
def index(limit=10,published:bool=True, sort:Optional[str]=None): #adding default values
    #only get 10 published blogs

    if published : 
        return {"data" : f"{limit} published blogs from the db"}
    else : 
         return {"data": f"{limit} blogs from the database"}
   


app.get("/blog/unpublished")

def unpublished ():
    return {"data": "all unpublished blogs"}


#fetching a single blog with id - dynamic routing
@app.get('/blog/{id}')

def show(id:int): #specifying the types of id we want to return
    return {'data':
       id
    }


@app.get('/blog/{id}/comments')

def comments(id, limit = 10): 
    return {"data" : {"1", "2"}}

class Blog(BaseModel):
   title: str
   body: str
   published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {"data":f"Blog is created as {request.title}"}

