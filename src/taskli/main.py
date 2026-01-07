import typer
from typing import Annotated
from taskli import Database, Status

app = typer.Typer()
db = Database()

def printTable(status: Status = None):
    tasks = db.getTasks(status)
    tmplt = "{:<4}|{:<30}|{:<15}"
    header = tmplt.format("ID","DESCRIPTION", "STATUS") #header
    print("-"*len(header))
    print(header)
    print("-"*len(header))
    for i in tasks:
        print(tmplt.format(i['id'],i['desc'],i['status']))
    print("-"*len(header))

@app.command()
def add(taskdesc: Annotated[str, typer.Argument(help="the task description")]):
    ''' ADD a new task '''
    db.addTask(taskdesc)
    printTable()
    
@app.command()
def delete(taskid: Annotated[str, typer.Argument(help="Enter the task's id")]):
    ''' DELETE a task using its id '''
    db.deleteTask(taskid)
    printTable()

@app.command()
def update(taskid: Annotated[int, typer.Argument(help="Enter the Task's id")],taskdesc: Annotated[str,typer.Argument(help="new DESCRIPTION for the task")]):
    ''' update/chanfe a task's descritption '''
    db.updateDesc(taskdesc,taskid)
    printTable()

@app.command()
def mark(taskid: Annotated[int,typer.Argument(help="Enter the task's id")],status: Annotated[Status,typer.Argument(help="change the status of a given task")]):
    ''' Update/Change a task's status [todo,done,in progress]'''
    db.updateStatus(status,taskid)
    printTable()

@app.command()
def list(status: Annotated[Status,typer.Argument(help="filter tasks by status")]=None):
    ''' show a table of tasks '''
    printTable(status)


if __name__ == "__main__":
    app()
