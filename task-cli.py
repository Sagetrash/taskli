import typer
import json_helpers as j
from classes.task import task, status
from typing import Annotated
app = typer.Typer()
lastId = j.lastId()


@app.command()
def add(desc: Annotated[str, typer.Argument()]):
    j.saveToJson(task(lastId+1,desc))

@app.command()
def mark(tid:Annotated[int,typer.Argument()],state: Annotated[status,typer.Argument()]):
    gotId = j.FindTaskId(tid)
    if gotId != -1:
        alltasks = j.openJson()
        alltasks[gotId]["status"] = state
        j.createJson(alltasks)
        print(f"marked task {tid}  as {state}")

if __name__ == "__main__":
    app()