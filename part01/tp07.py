
def f(*l):
    a,b,c = l
    print(l)
    print(a,b,c)

a = ['value 1','value 2','value 3']

t = 'value 1','value 2','value 3'
print(t)
print(a)

f(1,2,34)

# t1 = 1,2,3
# t1[0]=12

a,b=0,1
a,b,c,*d = 0,1,2,3,4,5

print(a,b,c,d)
print(d)

a = ['value 1','value 2','value 3']
for pos,value in enumerate(a):
    print(pos,value)

l = (0,"toto",15)


l = "toto",
print(l)