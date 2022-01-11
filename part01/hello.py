print("Hello")

# theWorldIsFlat => camelCase
# TheWorldIsFlat => PascalCase, UpperCamelCase, CapWords
# the_world_is_flat => snake_case
# the-world-is-flat => spin-case, train-case, kebab-case
the_world_is_flat = True
print(type(the_world_is_flat))
if the_world_is_flat:
    print("Be careful not to fall off!")

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!

text = "# This is not a comment because it's inside quotes."
text = '# This is not a comment because it\'s inside quotes.'

text="ligne 1\nligne 2"
text="ligne 1\tligne 2"
print(text)
path = "c:\toto\nono"
path = "c:\\toto\\nono"
path = r"c:\toto\nono"
print(path)

s = """
    ligne 1
    ligne 2
    ligne 3
"""
print(s)

a=2
b=3
s = "12"
d = int(s)
c = a+b 
print(type(a))
print(type(s))
s = "valeur de a : "+str(a)# 2 => "2"
s1 = "toto"
s2 = s+s1

print(50*'-')
print(s)

a = 50*'toto'
