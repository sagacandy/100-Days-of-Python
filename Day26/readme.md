# Writeline() method in python

If you want to write multiple lines to a file, you can use the writelines() method instead. This method takes a list of strings as input, and writes each string to the file as a separate line. Here's an example:

```python
# Open a file for writing
file = open('example.txt', 'w')

# Write multiple lines to the file
lines = ['This is the first line.\n', 'This is the second line.\n', 'This is the third line.\n']
file.writelines(lines)

# Close the file
file.close()
```

In this example, we open a file named example.txt for writing using the w mode. Then we create a list of strings, where each string is a separate line of text that we want to write to the file. Finally, we use the writelines() method to write all of the lines to the file, and then close the file.

Note that if the file already exists, opening it in write mode ('w') will overwrite the existing contents of the file. If you want to append new lines to the end of an existing file, you can open the file in append mode ('a') instead.

##Readline() method in python file io
To read the second or third line from a file using readline() method in Python, you can simply call the readline() method again after reading the first line. Each time you call readline(), it will read the next line in the file.

```python
# Open a file for reading
file = open('example.txt', 'r')

# Read the first line of the file
line1 = file.readline()

# Read the second line of the file
line2 = file.readline()

# Read the third line of the file
line3 = file.readline()

# Print the lines
print(line1)
print(line2)
print(line3)

# Close the file
file.close()
```

In this example, we read the first line of the file using readline() and store it in the variable line1. Then we call readline() two more times to read the second and third lines of the file, which are stored in the variables line2 and line3, respectively. Finally, we print all three lines.

If you want to read all the lines in the file, you can use a loop:

```python
# Open a file for reading
file = open('example.txt', 'r')

# Loop through the lines in the file
for line in file:
    print(line)

# Close the file
file.close()
```
