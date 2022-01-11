import json
import csv
import tabulate

def main():
    with open('todos2.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=';',quoting=csv.QUOTE_ALL)

        rows = list(reader)

        print(tabulate.tabulate(rows,headers="keys"))
def main_write_csv():
    
    with open('./ch10_2/todos.json') as f:
        todos = json.load(f)
    
    with open('todos2.csv', 'w', newline='') as csvfile:
        fieldnames = todos[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=';',quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(todos)


if __name__ == '__main__':
    main()