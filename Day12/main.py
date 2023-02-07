from functools import reduce


def cube(x):
    return (x*x*x)


print(cube(3))

l = [1, 2, 3, 4, 5, 6, 4]

# this is a very lengthy process
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

# we use map function
newl = list(map(cube, l))
print(newl)

# filter funtion


def test_filter(a):
    return (a > 10)


li = list(filter(test_filter, newl))
print(li)

# reduce funtion
num = [1, 2, 3, 4, 5]
numb = reduce(lambda r, s: r+s, num)
print(numb)
