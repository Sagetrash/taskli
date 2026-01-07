import sqlite3 as sql
from pathlib import Path
from typing import Annotated
from enum import Enum

class Status(str,Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

class Database:
    def __init__(self, db_path:Path = None):
        if db_path is None:
            db_path = Path(__file__).resolve().parent.parent.parent/"data"/"taskli.db"

        if db_path != ":memory:":
            db_path = Path(db_path)
            db_path.parent.mkdir(parents=True,exist_ok=True)
        self.conn = sql.connect(str(db_path))
        self.conn.row_factory = sql.Row
        self.createTable()
    
    def createTable(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            desc TEXT NOT NULL,
            status CHECK( status in ('todo','in-progress','done') ) DEFAULT 'todo',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            '''
        with self.conn:
            curs = self.conn.cursor()
            curs.execute(query)

    def getTasks(self, status:Status = None):
        query = "SELECT * FROM tasks"
        params = []
        if status:
            query += (" WHERE status = ?")
            params = (status.value,)
        try:
            with self.conn:
                curs = self.conn.cursor()
                curs.execute(query,params)
                tasks = curs.fetchall()
                rtn = []
                for i in tasks:
                    rtn.append(dict(i))
                return rtn
                    

        except sql.OperationalError as e:
            print(f"{e} \n creating a new table....")
            self.createTable()
            print(f"table Created!")

    def addTask(self,desc:str):
        query = '''
        INSERT INTO tasks (desc) VALUES (?);
        '''
        try:
            with self.conn:
                curs = self.conn.cursor()
                curs.execute(query,(desc,))
                self.getTasks()
        except sql.Error as e:
            print(f"{e}")

    def deleteTask(self,id:int):
        query = '''
            DELETE FROM tasks WHERE id = ?;
        '''
        try:
            with self.conn:
                curs = self.conn.cursor()
                curs.execute(query,(id,))
                self.getTasks()
        except sql.Error as e:
            print(f"{e}")
    
    def updateDesc(self,desc:str,id:int):
        query = '''
            UPDATE tasks SET "desc" = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?;
        '''
        try:
            with self.conn:
                curs = self.conn.cursor()
                curs.execute(query,(desc,id))
                self.getTasks()
        except sql.Error as e:
            print(f"{e}")

    def updateStatus(self,status:Status, id:int):
        query = '''
            UPDATE tasks SET "status" = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?;
        '''
        try:
            with self.conn:
                curs = self.conn.cursor()
                curs.execute(query,(status,id))
                self.getTasks()
        except sql.Error as e:
            print(f"{e}")

if __name__ == "__main__":
    pass