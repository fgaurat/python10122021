
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(max_value=10):    # return Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    a, b = 0, 1
    l = []
    while a < max_value:
        l.append(a)
        a, b = b, a+b

    return l


# Now call the function we just defined:
fib(2000)

print(fib)

f = fib

f(100)

l = fib2()
print(l)
# l = [0,1,1,2,3,5,8,13,21,34,55,89]
# l =[]
# print(l)
# l.append(10)
# l.append(10)
# print(l)

i=[]

def f(value,arg=i):
    arg.append(value)
    return arg

def f(value,arg=None):
    if arg == None:
        arg = []
    arg.append(value)
    return arg
l = [12,56]
a = f(1,l) # [12,56,1]
print(a)
a = f(2) # [2] ou [1,2]
print(a) 
a = f(3)
print(a) 

print(50*"-")
a = fib2(max_value=10)
print(a) 
print(50*"-")

def sayHello(name,firstName,age=60):
    print("hello",name,firstName,age)


sayHello('DUPONT','Robert',60)
sayHello(firstName='Robert',name='DUPONT')
sayHello('DUPONT',age=60,firstName='Robert')

print(50*"-")

def add_1(l):
    r = 0
    for i in l:
        r+=i
    return r
def add(*l):
    print(l)
    r = 0
    for i in l:
        r+=i
    return r

int_l = [1,2,3,4]
r = add(*int_l) # 10
print(r)
r = add_1([1,2,3,4,5]) # 10
r = add(1,2,3,4,5) # 10
print(r)
print(50*"-")

def sayHello(**d):
    print(d['firstName'])
    name = d['name']
    firstName = d['firstName']
    age = d['age']
    print("hello",name,firstName,age)


# sayHello('DUPONT','Robert',60)
sayHello(firstName='Robert',name='DUPONT', age=60)
sayHello(name='DUPONT',age=60,firstName='Robert')

d = {'name': 'DUPONT', 'age': 60, 'firstName': 'Robert'}
sayHello(**d)
print(50*'-')

def f(*args,**kwargs):
    print("args",args)
    print("kwargs",kwargs)
    print()

f(1,2,3)
f(59,87,name="toto",age=56)
print(50*'-')

#Positional only
# def sayHello(name,firstName,/):
def sayHello(*,name,firstName):
    print(firstName)
    print(name)

# sayHello('DUPONT','Robert')
sayHello(name='DUPONT',firstName='Robert')
