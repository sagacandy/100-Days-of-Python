def square(x): return x**2


result = square(5)
print(result)   # Output: 25

# to filter the even number using lambda and filer function

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, num)
print(list(even_numbers))

# to filter the odd numbers using filter function in python
numbers = list(range(11, 21))
odd_numbers = list(filter(lambda y: y % 2 == 1, numbers))
print(odd_numbers)
