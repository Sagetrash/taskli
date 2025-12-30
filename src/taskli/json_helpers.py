from .classes.task import task
import json, os
directory = '.'
path = f"{directory}/tasks.json"

def openJson()->list:
    if os.path.exists(f"{path}"):
        try:
            with open(path,'r') as f:
                alltasks = json.load(f)    
                return alltasks
        except json.JSONDecodeError as e:
            if input("error decoding file, do you want to make a new tasks.json file? (y/n): ") =='y':
                alltasks = []
                createJson(alltasks)
                return []
            else:
                print("no problem! hope you find your file!")
    else:
        createJson()
        return []

def saveToJson(task:task):
    alltasks = openJson()
    try:
        FindTaskId(task.taskdict["id"])
        print("task already present")
    except IndexError:
        alltasks.append(task.taskdict)
    finally:
        createJson(alltasks)

    
def setDir(setpath:str):
    global directory
    directory = setpath

def createJson(arg = None):
    if arg is None:
        if not os.path.exists(path):
            try:
                with open(path,'w') as f:
                    alltasks = []
                    json.dump(alltasks,f,indent=4)
            except json.JSONDecodeError as e:
                print(f"error saving file {e}")
        else:
            print("file already exists")
    else:
        try:
            with open(path,'w') as f:
                json.dump(arg,f,indent=4)
        except json.JSONDecodeError as e:
            print(f"error saving file {e}")

def FindTaskId(tid:int,alltasks:list=openJson())-> int:
    for i in alltasks:
        if i['id'] == tid:
            # print("task already exists")
            return alltasks.index(i)
    raise IndexError    

def lastId():
    try:
        last = openJson()[-1]["id"]
    except IndexError as e:
        last = 0

    return last