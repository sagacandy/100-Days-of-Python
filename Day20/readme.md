_Match Case in Pyhton_

In Python, the match statement is used to perform pattern matching on values. It is a new feature introduced in Python 3.10. Here's an example of how to use match in Python:

```pyhton
match value:
    case pattern1:
        # code to run when value matches pattern1
    case pattern2:
        # code to run when value matches pattern2
    case _:
        # code to run when value does not match any previous patterns

```

In the example above, value is the value to match against, and pattern1 and pattern2 are patterns that value might match. The \_ case is a catch-all case that matches anything that doesn't match any previous patterns.
Each case block can contain any valid Python code, including multiple lines of code or function calls.
