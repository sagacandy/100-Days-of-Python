In day 4 I learned following things:
Difference between print() and return()
print() is used to output a value to the console and return() is used to return a value from a function to the caller. While print() statement is used for debugging, testing and for the user to see the outcome, return() statement is used for the function to return value that will be used in the further operations.
"Finally:" keyword in try-except-finally block and difference between finally: and using print function. example:

```python
    try:
        # some code that may raise an exception
        x = 1/0
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        # code that will always be executed, even if an exception is raised
        print("Cleaning up resources.")
```

In this example, the code in the try block will raise a ZeroDivisionError exception because it attempts to divide by zero. The except block will catch this exception and print "Cannot divide by zero." However, the code in the finally block will still be executed and will print "Cleaning up resources." regardless of the exception.
