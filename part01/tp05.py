

def mult2(v:int)->int:
    """
    return v *2
    """
    return v*2


a = [1,2,3,4,5]

b=[]
for i in a:
    v = mult2(i)
    b.append(v)
print(b)

b = map(mult2,a)
# list_b = list(map(mult2,a))

for i in b:
    print(i)

b = list(map(lambda v:v*2,a))
print(b)
# b = [2,4,6,8,10]


print(50*'-')
a = [1,2,3,4,5]
def mult22(value):
    return value*2
c = map(mult22,a)

for i in c:
    print(i)
print(50*'-')
for i in c:
    print(i)



names = ['   toto  ','titi   ','   tatat   ']
names = list(map(lambda s: s.strip(),names))
print(names)



