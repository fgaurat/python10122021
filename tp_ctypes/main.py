from ctypes import CDLL,c_char_p

def main():
    libc = CDLL('hello.o')
    libc.sayHello()

    libc.hello(c_char_p(b"Fred"))

if __name__ == '__main__':
    main()