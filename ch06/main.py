# from fibo import fib2,fib
from fibo import fib
import fibo
import sys


# from fibo import fib as remote_fib


# def fib(n):
#     print("local fib",n)


def main():
    print("module main name: ",__name__)
    # fibo.fib(1000)
    # a = fibo.fib2(1000)
    # fi.fib(1000)
    # a = fi.fib2(1000)
    # print(a)
    # fi.fib(1000)
    # remote_fib(1000)

    params = [int(p) for p in sys.argv[1:]]
    print(sys.argv[1:])
    print(params)

    for i in params:
        fib(i)
    # fibo.fib(p)



if __name__ == "__main__":
    main()




