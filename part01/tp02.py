
squares = [1, 4, 9, 16, 25]


print(squares)

print(squares[0])
print(squares[-1])
print(squares[2:5])
print(squares[:5])
print(squares[2:])

print(squares)
print(squares[:])

squares2=squares[:]
squares[0]=1000
print(squares)
print(squares2)

la_liste = [
    [0,1,2],
    [3,4,5],
]


la_liste2 = la_liste[:]
print(la_liste)
print(la_liste[0][1])
la_liste[0][1] = 1000
print(la_liste)
print(la_liste2)

squares = [1, 4, 9, 16, 25]
squares2 = squares
squares[0]=1000
print(squares)
print(squares2)
squares2 = squares[:]
squares[0]=2000
print(squares)
print(squares2)




a = [[0,1],[2,3],[4,5]]
b=a[:]

a[0][0]=1000
print(a)
print(b)
print(50*'-')

a = [0,1,2,3]
b = [4,5,6,7]
c = a+b
print(c)
print(50*'-')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters = "abcdefg"
print(letters[2:5])
letters[2:5] = [0,1,2]
print(letters)


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


