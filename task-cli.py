import typer
import json_helpers as j
from classes.task import task, status
from typing import Annotated
from datetime import datetime

app = typer.Typer()
lastId = j.lastId()


@app.command()
def add(desc: Annotated[str, typer.Argument()]):  
    j.saveToJson(task(lastId+1,desc))
    lst()

@app.command()
def mark(state: Annotated[status,typer.Argument()], tid:Annotated[int,typer.Argument()]):
    gotId = j.FindTaskId(tid)
    if gotId != -1:
        alltasks = j.openJson()
        alltasks[gotId]["status"] = state
        alltasks[gotId]["last_updated"] = datetime.now().ctime()
        j.createJson(alltasks)
        print(f"marked task {tid}  as {state}")

@app.command()
def lst(state: Annotated[status, typer.Argument()]=None):
    alltasks = j.openJson()
    try:
        headers = list(alltasks[0].keys())
        for k in headers:
            print(k,end=" | ")
        print("")
        if state is None:
            for i in alltasks:
                data = list(i.values())
                for k in data:
                    print(k,end=" | ")
                print("")
        else:
            for i in alltasks:
                if i["status"] == state:
                    for k in list(i.values()):
                        print(k,end=' | ')
                    print("")
    except IndexError:
        None


@app.command()
def update(tid: Annotated[int,typer.Argument()], desc: Annotated[str,typer.Argument()]):
    alltasks = j.openJson()
    try:
        taskindex = j.FindTaskId(tid)
        alltasks[taskindex]["desc"] = desc
        alltasks[taskindex]["last_updated"] = datetime.now().ctime()
        j.createJson(alltasks)
        lst()
    except IndexError:
        print("enter valid id")
        lst()


@app.command()
def delete(tid: Annotated[int, typer.Argument()]):
    alltasks = j.openJson()
    try:
        index = j.FindTaskId(tid,alltasks)
        deleted = alltasks.pop(index)   
        for i in range(index,len(alltasks)):
            alltasks[i]["id"] -= 1
        j.createJson(alltasks)
        print(f"deleted task {deleted}")
        lst()
    except IndexError as e:
        print("invalid taskid")

if __name__ == "__main__":
    app()
