a=input("Enter the 'quit' or any desired string: ")
if a=='quit':
    print("You have entered 'quit'")
else:
    raise ValueError (f"You have entered {a} which is invalid")