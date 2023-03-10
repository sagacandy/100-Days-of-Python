# OS module in Python

The os module in Python provides a way to interact with the operating system. It allows you to perform various system-related tasks, such as working with files and directories, manipulating the environment, and running system commands.

The code in main.py shows how I created Day1 to Day100 directories and also created readme.md file inside every Day{n} directories

Here are some of the key functions and attributes provided by the os module:

1. os.getcwd(): Returns the current working directory as a string.
2. os.chdir(path): Changes the current working directory to the specified path.
3. os.listdir(path="."): Returns a list of filenames in the specified directory, or the current directory if none is specified.
4. os.mkdir(path, mode=0o777, \*, dir_fd=None): Creates a new directory with the specified path and mode.
5. os.remove(path, \*, dir_fd=None): Removes the file at the specified path.
6. os.rename(src, dst, \*, src_dir_fd=None, dst_dir_fd=None): Renames the file or directory at the src path to the dst path.
7. os.environ: A dictionary representing the environment variables for the current process.
8. os.system(command): Runs the specified command in a subshell.

Here's an example of using some of the os module functions to work with files and directories:

```python
import os

# Print the current working directory
print("Current directory:", os.getcwd())

# Create a new directory
os.mkdir("testdir")

# Change the current working directory to the new directory
os.chdir("testdir")

# Create a new file and write some data to it
with open("testfile.txt", "w") as f:
    f.write("Hello, world!")

# List the contents of the directory
print("Contents of directory:", os.listdir())

# Rename the file
os.rename("testfile.txt", "newfile.txt")

# Remove the file and directory
os.remove("newfile.txt")
os.chdir("..")
os.rmdir("testdir")


```

This code creates a new directory called testdir, changes the current working directory to the new directory, creates a new file called testfile.txt and writes some data to it, lists the contents of the directory, renames the file to newfile.txt, removes the file and directory, and finally changes the current working directory back to the original directory.
