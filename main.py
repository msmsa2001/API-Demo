from fastapi import FastAPI, Body

import schema

app=FastAPI()

fakeDatabase={
    1:{'task':'Clean car'},
    2:{'task':'Write blog'},
    3:{'task':'Startt stream'}
}

@app.get("/")
def  getItem():
    # return ['Sadique','Ali','Mansuri'] 
    return fakeDatabase

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id]

# @app.post("/")
# def addItem(taks:str):
#     newId=len(fakeDatabase.keys()) +1
#     fakeDatabase[newId]={"task":taks}
#     return fakeDatabase


# @app.post("/")
# def addItem(item:schema.Item):
#     newId=len(fakeDatabase.keys()) +1
#     fakeDatabase[newId]={"task":item.task}
#     return fakeDatabase


@app.post("/")
def addItem(body=Body()):
    newId=len(fakeDatabase.keys()) +1
    fakeDatabase[newId]={"task":body['task']}
    return fakeDatabase

@app.put("/{id}")
def updateItem(id:int,item:schema.Item):
    fakeDatabase[id]['task']=item.task
    return fakeDatabase

@app.delete("/{id}")
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase