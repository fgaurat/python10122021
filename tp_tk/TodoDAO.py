import sqlite3

from Todo import Todo


class TodoDAO:


    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)
    
    def save(self,todo):
        cur = self._con.cursor()
        sql = f"INSERT INTO todos_tbl(title,completed,user_id) VALUES ('{todo.title}',{todo.completed},{todo.userId})"
        cur.execute(sql)
        todo.id = cur.lastrowid
        self._con.commit()        

    def findAll(self):
        cur = self._con.cursor()

        results = cur.execute('SELECT id,user_id,title,completed FROM todos_tbl')

        # todos = [Todo(*data) for data in results]
        # todos = []
        # for data in results:
        #     todo = Todo(*data)
        #     todos.append(todo)
        # return todos

        for data in results:
            todo = Todo(*data)
            yield todo


    def __del__(self):
        self._con.close()