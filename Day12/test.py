# another usage of filter funtion to find if the number is even
from functools import reduce


def iseven(x):
    return (x % 2 == 0)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newl = list(filter(iseven, l))
print(newl)

# Injecting lambda with map function which is known as passing function as an argument
li = [1, 2, 3, 4, 5]
newli = list(map(lambda x: x*x*x, li))
print(newli)

# reduce function in python
num = [1, 2, 3, 4, 5]
numb = reduce(lambda r, s: r+s, num)
print(numb)

# reduce example 2 by using defining funtion


def mul(f, g):
    return (f*g)


number = reduce(mul, num)
print(number)
