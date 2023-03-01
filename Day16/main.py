def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))


print(factorial(5))


def f(a):
    if a <= 1:
        return 1
    else:
        return f(a-1) + f(a-2)


print(f(6))
