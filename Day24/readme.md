# Python File IO

In Python, the open() function is used to open files. The second argument to the open() function specifies the mode in which the file is opened. Here are the different modes that can be used with the open() function:

The code in main.py shows how I created Day1 to Day100 directories and also created readme.md file inside every Day{n} directories

Here are some of the key functions and attributes provided by the os module:

1. Read mode ('r'): This is the default mode. It is used to open a file for reading. If the file doesn't exist, an error will be raised.
2. Write mode ('w'): This mode is used to open a file for writing. If the file already exists, it will be truncated (emptied). If the file doesn't exist, a new file will be created.
3. Append mode ('a'): This mode is used to open a file for writing, but the data will be appended to the end of the file instead of overwriting the existing data. If the file doesn't exist, a new file will be created.
4. Binary mode ('b'): This mode is used to open a file in binary mode. It is used for non-text files like image and audio files.
5. Exclusive creation mode ('x'): This mode is used to open a file for exclusive creation. If the file already exists, an error will be raised.

Modes can be combined by specifying them as separate characters in the second argument to <open()>. For example, 'wb' is a valid mode for opening a file for writing in binary mode.

```python
# Open the file in write mode
file = open('example.txt', 'w')

# Write to the file
file.write('Hello World!')

# Close the file
file.close()

# Open the file in read mode
file = open('example.txt', 'r')

# Read the contents of the file
content = file.read()

# Close the file
file.close()

# Print the contents of the file
print(content)



```

In this example, we first write the string "Hello World!" to the file using the write() method of the file object, and then close the file using the close() method.

Then we open the same file in read mode using the open() function, read the contents of the file using the read() method of the file object, and store the contents in the content variable. Finally, we close the file using the close() method of the file object and print the contents of the file to the console using the print() function.

This code will output "Hello World!" to the console.
