a = int(input("Enter the number between 5 and 10: "))
if not (a > 5 and a < 10):
    raise ValueError("Value should be between 5 and 10")
