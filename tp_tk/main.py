from tkinter import *
from tkinter import ttk
import configparser
import argparse

from TodoDAO import TodoDAO


def sayHello():
    print("Hello")

def main(db_file):
    root = Tk()
    dao = TodoDAO(db_file)
    tree = ttk.Treeview(root,columns=('id','userId','title','completed'),show="headings")
    tree.heading('id',text="#")
    tree.heading('userId',text="userId")
    tree.heading('title',text="title")
    tree.heading('completed',text="completed")

    for todo in dao.findAll():
        tree.insert("",index=todo.id,values=[todo.id,todo.userId,todo.title,todo.completed])
    tree.pack(fill=BOTH,expand=True)

    root.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(    description = 'SQLlite example')
    parser.add_argument('config_file',help="Config file")
    args = parser.parse_args()
    config = configparser.ConfigParser()
    config.read(args.config_file)
    db_file = config['DB']['db_file']
    main(db_file)    

