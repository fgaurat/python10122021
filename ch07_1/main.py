def main():
    


    with open("hello.txt","w") as f:
        # f.write("Hello 1\n")
        # f.write("Hello 2\n")
        print("Hello 1",file=f)
        print("Hello 2",file=f)
    

    # with open("hello.txt","r") as f:
    with open("hello.txt") as f:
        # s = f.read()
        # print(s)
        # l = [d.strip() for d in f.readlines()]
        # print(l)
        for line in f:
            print(line.strip())

    


if __name__ == '__main__':
    main()