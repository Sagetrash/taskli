from classes.task import task
import json, os
directory = '.'
path = f"{directory}/tasks.json"

def openJson():
    if os.path.exists(f"{path}"):
        try:
            with open(path,'r') as f:
                alltasks = json.load(f)    
                return alltasks
        except json.JSONDecodeError as e:
            if input("error decoding file, do you want to make a new tasks.json file? (y/n): ") =='y':
                alltasks = []
                createJson(alltasks)
                return openJson()
            else:
                print("no problem! hope you find your file!")
    else:
        createJson()
        return openJson()

def saveToJson(task:task):
    alltasks = openJson()
    if FindTaskId(task.taskdict['id'],alltasks) == -1:
        alltasks.append(task.taskdict)
        createJson(alltasks)
    else:
        "task already exists"

    
def setDir(setpath:str):
    global directory
    directory = setpath

def createJson(arg = None):
    if arg is None:
        if not os.path.exists(path):
            try:
                with open(path,'w') as f:
                    alltasks = []
                    json.dump(alltasks,f)
            except json.JSONDecodeError as e:
                print(f"error saving file {e}")
        else:
            print("file already exists")
    else:
        try:
            with open(path,'w') as f:
                json.dump(arg,f)
        except json.JSONDecodeError as e:
            print(f"error saving file {e}")

def FindTaskId(tid:int,alltasks:list=openJson()):
    for i in alltasks:
        if i['id'] == tid:
            # print("task already exists")
            return alltasks.index(i)
    # print("creating new task")
    return -1

def lastId():
    try:
        last = openJson()[-1]["id"]
    except IndexError as e:
        last = 0

    return last