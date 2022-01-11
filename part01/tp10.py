
d = {"name":"DUPONT","firstName":"Robert"}
print(d)
print(d['name'])
print(d['firstName'])


names = ['name','firstName']
values = ['DUPONT','Robert']

d = dict(zip(names,values))
print(d)
# d = {"name":"DUPONT","firstName":"Robert"}

d = {}
for i in range(len(names)):
    d[names[i]] = values[i]
print(d)

d = {names[i]:values[i] for i in range(len(names))}

print(d)
print(50*'-')
for k in d:
    print(k, d[k])

l = list(d)
print(l)

print(d.keys())
print(d.values())
print(d.items())

for k,v in d.items():
    print(k,v)