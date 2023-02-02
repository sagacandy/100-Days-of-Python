x = 5


def hello():
    global x
    x = 4
    print("THis is  saga hi")
    print(f"This is local variable x inside function value is {x}")


hello()
print(f"This is a global variable whose value is {x}")
