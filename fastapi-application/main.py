from fastapi import FastAPI
import uvicorn


app = FastAPI()



@app.post('/')
def hello_func(hello: str):
    ...
    



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)