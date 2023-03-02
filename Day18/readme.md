# Here are some common dictionary methods in Python with examples:

1. dict.get(key, default=None) - Returns the value for the given key if it exists in the dictionary, else returns the default value (which is None if not specified).

2. dict.keys() - Returns a view object of all the keys in the dictionary.

3. dict.values() - Returns a view object of all the values in the dictionary.

4. dict.items() - Returns a view object of all the key-value pairs in the dictionary as tuples.

5. dict.pop(key, default=None) - Removes the key-value pair for the given key from the dictionary and returns the value. If the key is not found and a default value is specified, it returns the default value, otherwise it raises a KeyError.

6. dict.update(other_dict) - Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.

7. dict.clear() - Removes all the key-value pairs from the dictionary.

8. dict.copy() - Returns a shallow copy of the dictionary.

9. len(dict) - Returns the number of key-value pairs in the dictionary.

10. dict.setdefault(key, default=None) - Returns the value for the given key if it exists in the dictionary, else sets the key to the default value (which is None if not specified) and returns the default value.

```python
d1 = {1: 1, 2: 4, 3: 9, 4: 16}
d2 = {5: 25, 6: 36, 7: 49}
d1.update(d2)
d1.pop(2)
d1.popitem()
# d1.clear()
print
print(len(d1))

```
