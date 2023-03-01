# Here are some common string methods in Python with examples:

1. upper() - converts all characters in a string to uppercase.

```python
string = "hello world"
new_string = string.upper()
print(new_string)  # Output: "HELLO WORLD"
```

2. lower() - converts all characters in a string to lowercase.

```python
string = "Hello World"
new_string = string.lower()
print(new_string)  # Output: "hello world"
```

3. strip() - removes leading and trailing whitespace characters from a string.

```python
string = "    Hello World    "
new_string = string.strip()
print(new_string)  # Output: "Hello World"
```

4. replace() - replaces all occurrences of a specified substring with another substring.

```python
string = "hello world"
new_string = string.replace("world", "python")
print(new_string)  # Output: "hello python"
```

5. split() - splits a string into a list of substrings based on a specified delimiter.

```python
string = "hello,world"
new_list = string.split(",")
print(new_list)  # Output: ["hello", "world"]
```

6. startswith() - checks if a string starts with a specified substring.

```python
string = "hello world"
result = string.startswith("hello")
print(result)  # Output: True

```

7. endswith() - checks if a string ends with a specified substring.

```python
string = "hello world"
result = string.endswith("world")
print(result)  # Output: True

```
