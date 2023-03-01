a = "Sagar Khatri"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("r"))
print(a.replace("Khatri", "Sagar"))
print(a.split(" "))  # list
print(type(a.split(" ")))

heading = "this is Python"
print(heading.capitalize())

print(heading.count("i"))  # count number of specific letters
print(heading.find("saga"))  # can handle not found errors
print(heading.index("is"))  # cannot find not found errors
