
word = "Python"
print(word)
print(len(word))

print(word[len(word)-1])
print(word[-1])

print(word[-6])
print(word[0])
print(word[2:5])

print(word[:3])
print(word[3:])
print(word[-2:])

print(word[45:58])

# word[0] = 'J'
# print(word)


word = "Python"
word1=word
word2="Python"

word3 = 'J'+word[1:]

print(hex(id(word)))
print(hex(id(word1)))
print(hex(id(word2)))
print(word3)
print(hex(id(word3)))

print(50*'-')
a=1
b=1
print(hex(id(a)))
print(hex(id(b)))
b=2
print(hex(id(b)))


# print(50*'-')
# a1 = True
# b1 = True
# print(hex(id(a1)))
# print(hex(id(b1)))

