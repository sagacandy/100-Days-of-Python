# Recursion in Python

Recursion in Python is a technique that allows a function to call itself. A recursive function is a function that solves a problem by calling itself with a smaller instance of the same problem. The process continues until the problem can be solved without further recursion.

## Usage/Examples

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

```

## Explanation of above code

In this function, the base case is when n equals 0, and the function returns 1. The recursive case is when n is greater than 0, and the function calls itself with n-1. The process continues until n is equal to 0, at which point the function returns 1.
