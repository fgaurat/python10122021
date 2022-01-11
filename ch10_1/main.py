import requests
import json
import sqlite3
import configparser
import argparse

from TodoDAO import TodoDAO
from Todo import Todo

def main_save(db_file):
    dao = TodoDAO(db_file)
    todo = Todo(id=0,userId=1,title="Le titre de la todo",completed=False)
    dao.save(todo)
    print(todo,todo.id)

def main(db_file):

    dao = TodoDAO(db_file)
    d = list(dao.findAll())
    print(d)
    # for todo in dao.findAll():
    #     print(todo)


def main_select(db_file):
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        # results = cur.execute('SELECT id,user_id,title,completed FROM todos_tbl')

        # for id,user_id,title,completed in results:
        #     print(id,user_id,title,bool(completed))

        results = cur.execute('SELECT id,user_id,title,completed FROM todos_tbl WHERE completed=1')

        for id,user_id,title,completed in results:
            print(id,user_id,title,bool(completed))


def main_insert(db_file):

    with sqlite3.connect(db_file) as con:
        cur = con.cursor()

        with open("./ch10_1/todos.json") as f:
            todos = json.load(f)
            for todo in todos:
                
                # sql=f"INSERT INTO todos_tbl(title,completed,user_id) VALUES ('{todo['title']}',{todo['completed']},{todo['userId']})"
                sql="INSERT INTO todos_tbl(title,completed,user_id) VALUES ('{title}',{completed},{userId})".format(**todo)
                # print(sql)                
                cur.execute(sql)
        con.commit()


# def main():
#     r = requests.get('http://jsonplaceholder.typicode.com/todos')
#     todos = r.json()
    

#     for todo in todos:
#         print(todo['title'])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(    description = 'SQLlite example')
    parser.add_argument('config_file',help="Config file")
    args = parser.parse_args()
    print(args.config_file)

    config = configparser.ConfigParser()
    config.read(args.config_file)
    print(config['DB']['db_file'])
    db_file = config['DB']['db_file']
    # main(db_file)