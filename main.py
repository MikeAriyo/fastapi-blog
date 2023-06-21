from fastapi import FastAPI  #importing

app = FastAPI(); #creating an instance of fastapi

@app.get('/blog')  #(/) base path

#path operator function
def index(limit,published): 
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

def comments(id): 
    return {"data" : {"1", "2"}}
