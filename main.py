from fastapi import FastAPI

app = FastAPI() # creating an instance

def index():
    return 'heyy'