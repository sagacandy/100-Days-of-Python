# Lamdba in python

In Python, a lambda function is a small, anonymous function that can be defined in a single line of code. It is sometimes also called an "inline function" or a "lambda expression".

Lambda functions are typically used when you need a simple function for a short period of time and don't want to define a separate named function for it. Lambda functions are especially useful when you want to pass a function as an argument to another function, such as the map(), filter(), or reduce() functions.

The syntax for defining a lambda function is as follows:

```python
lambda arguments: expression

```

Here, arguments is a comma-separated list of the function's input arguments, and expression is the single expression that the function evaluates and returns.

Example

```python
square = lambda x: x**2
```

In this example, we define a lambda function that takes one argument x and returns the square of x. We assign this function to a variable named square.

You can call a lambda function just like any other function. For example:

```python
result = square(5)
print(result)   # Output: 25
```

In this example, we call the square() function with an argument of 5, which returns 25. We assign this value to a variable named result, and then print it to the console.

## Filter() function

In Python, the filter() function is used to filter elements from a sequence (e.g., list, tuple, or string) based on a condition defined by a function. The syntax for using the filter() function is as follows:

```python
filter(function, sequence)
```

Here, function is the function that defines the condition for filtering, and sequence is the sequence of elements to be filtered. The filter() function returns an iterator that contains the filtered elements.
