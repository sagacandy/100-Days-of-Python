# readlines() method usage to read all line and datatype is list(string)
f = open('test2.txt', 'r')
lines = f.readlines()
print(lines)
f.close()

# to read a specific line
f = open('test2.txt', 'r')
line3 = lines[2]
print(line3)
f.close()

# writeline() method
f = open('test2.txt', 'a')
line = ("This is 5th line")
f.writelines(line)
f.close()
