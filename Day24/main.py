file = open('test1.txt', 'x')
file.write("This file is created and written usinng python")
file.close()

file = open('test1.txt', 'r')
content = file.read()
file.close()
print(content)
