s = {"valeur 1","valeur 2","valeur 3","valeur 2","valeur 1"}
s1 = {"valeur 10","valeur 2","valeur 35","valeur 4","valeur 7"}
s.add("valeur 7")
s.add("valeur 1")
print(s)

l = list(s)
l.sort()
print(l)

s3 = s & s1
print(s3)

s = {"valeur "+str(v) for v in range(10)}
print(s)


