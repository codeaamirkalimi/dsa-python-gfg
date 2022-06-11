import random

if 5 < 2:
    print("hello world")
else:
    print('bye bye')

# variables are created only when value is assigned
# python will ignore the string literals that are not assigned to a variable
"""
This is one way to write multi line comment
"""
print("Hello Aamir Kalimi")
a = 5
print(a)

# multi variable assignment make sure to balance the variable name with value
x, y, z = "Aamir", "Kalimi", "Sabir"
print(z)
x = y = z = "Aamir", "Kalimi", "Sabir"
print(x)
print(type(x))
fruits = ["banana", "apple", "cherry"]
a, b, c = fruits;
print(a)
print(type(a))
m, n = 5, 10
print(m + n)
o, p = "Aamir", 10
print(o, p)
globalVariable = "World"


def printVariable():
    global globalVariable
    globalVariable = "Hi"
    print(globalVariable)


printVariable()

high = 111111111111111111111111111111113333333333555555555566666666666665555555543333345
print(high)
print(random.randrange(0, 10))

# casting done in python in the constructor
