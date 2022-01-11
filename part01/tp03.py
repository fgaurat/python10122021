# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')



words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word)


for i in range(5):
    print(i)


for i in range(len(words)):
    print(str(i)+" "+words[i])
    print(i,words[i])


# 0 cat
# 1 window
# 2 defenestrate

print(list(range(5)))


l = [1,2,3,4]
print(sum(l))

print(50*"-")

for i in range(10):
    print(i)
    if i >3:
        break
else:
    print("else")

for i in range(10):
    pass

    # if i == 5:
    #     continue
    # print(i)