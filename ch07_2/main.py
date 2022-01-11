

def main():
    with open("todos.csv") as fichier: 
        keys = fichier.readline().strip().split(';')
        dictionnaire = [dict(zip(keys, line.strip().split(';'))) for line in fichier ]
    print(dictionnaire)    
    
def main_1():
    print("Lecture CSV")
    # open todos.csv en lecture
    end = []
    with open('todos.csv') as f:
        lines = f.readlines()
        # 1ere ligne= clefs du dict
        header = lines[0].strip()
        header = header.split(';')
        data = lines[1:]
        # for line in data
        for line in data:
            line = line.strip()
            l = line.split(";")
            d = dict(zip(header,l))
            end.append(d)
    
    print(end)
            


        # les autres lignes data
        # ligne.split(';') => ['data1','data2','data3',...]


def main_write_csv():
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

    with open("todos.csv",'w') as f:   
        headers = data[0].keys()
        line = ";".join(headers)
        print(line,file=f)
        for d in data:
            data = d.values()
            line = "{};{};{};{}".format(*data)
            print(line,file=f)









    # with open("todos.csv",'w') as f:   
    #     for d in data:
    #         data = d.values()
    #         s =""
    #         for i in range(len(data)):
    #             s+="{};"
    #         print(s)
    #         # line = "{};{};{};{}".format(*data)
    #         line = s[:-1].format(*data)
    #         print(line)
    #         # print(line,file=f)

    # for d in data:
    #     # values = []
    #     # for v in d.values():
    #     #     values.append(str(v))

    #     values = [str(v) for v in d.values()]
    #     print(";".join(values))



        # print(d.keys())
        
        # data = d.values()
        # line = "{};{};{};{}".format(*data)
        # print(line)

 
    # def printDataInCSV2(aData):
    # # ouverture du fichier
    #     with open("data.csv", "w") as fichier: 
    #         # Ecriture de l'entête
    #         print(';'.join(aData[0].keys()), file=fichier)
    #         # Ecriture des valeurs 
    #         for dictionnaire in aData:
    #             print(';'.join([str(value) for key, value in dictionnaire.items()]), file=fichier)
       

if __name__ == '__main__':
    main()
