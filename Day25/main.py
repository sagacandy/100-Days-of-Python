import os
if os.path.exists('test2.txt'):
    print("The file already exist")
    f = open('test2.txt', 'r')
    content = f.read()
    print(f"The content of file is: {content}")
    f.close()
else:
    f = open('test2.txt', 'x')
    f.write("This file is created and written using python")
    f.close()
# read the newly created file
    f = open('test2.txt', 'r')
    content = f.read()
    f.close()
