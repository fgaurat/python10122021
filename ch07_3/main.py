import json

def main():
    with open('todos.json','r') as f:
        data = json.load(f)
        print(data[0])
        print(data[0]['title'])
    


def main_write_json():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        }
    ]
    print(type(data))
    print(type(json.dumps(data)))
    with open('todos.json','w') as f:
        json.dump(data,f)

if __name__ == '__main__':
    main()
    
