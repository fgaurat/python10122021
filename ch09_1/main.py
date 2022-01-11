import json
from Todo import Todo
from pprint import pprint


def main():
    todos = []
    with open('todos.json','r') as f:
        data = json.load(f)
        for d in data:
            todo = Todo(**d)
            todos.append(todo)
    
    for todo in todos:
        print(todo)
    
    pprint(todos)

if __name__ == '__main__':
    main()