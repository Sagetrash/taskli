from datetime import datetime
from enum import Enum, auto

class task:
    def __init__(self,taskid:int,desc:str):
        self.taskdict = {
            "id":taskid,
            "desc":desc,
            "created_at":datetime.now().ctime()
        }
        self.taskdict["last_updated"] = self.taskdict["created_at"]
        self.taskdict["status"] = "todo"

    def __call__(self):
        return self.taskdict

class status(str,Enum):
    todo = "todo"
    done = "done"
    in_progress = "in-progress"