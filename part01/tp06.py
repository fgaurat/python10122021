from collections import deque


l = ["valeur 1","valeur 2","valeur 3"]

print(l)
l.append("valeur 4")
print(l)
p = l.pop()
print(p)
print(l) 
p = l.pop(0)
print(p)
print(l)
l.insert(0,"valeur 1 insert") 
print(l)

d =deque(l)

print(d)
d.appendleft('valeur 0')
print(d)
print(l)

a = [1,2,3,4,5]
b=[]
for i in a:
    v = i*2
    b.append(v)

b = [i*2 for i in a]
print(b)

names = ['   toto  ','titi   ','   tatat   ']
# names = list(map(lambda s: s.strip(),names))
names = [s.strip() for s in names]
print(names)


print(50*'-')
iter_1 = ['valeur de a :','valeur de b :','valeur de c :','valeur de d :']
iter_2 = [12,23,58,98]


# valeur de a : 12
# valeur de b : 23

# z = list(zip(iter_1,iter_2))
# print(z)
z = zip(iter_1,iter_2)

for elem in z:
    print(elem)
    print(elem[0],elem[1])

print(*[s.strip() for s in names])


# a= 2
# del a
# print(a)

a = ["toto","titi","tutu"]
print(a)
# del a[0]
a.remove("toto")
print(a)