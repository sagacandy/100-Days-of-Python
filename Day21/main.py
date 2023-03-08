while True:
    try:
        num = int(input("Enter the number to find multiplication: "))
        break
    except ValueError:
        print("Please enter integer")

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
    i += 1
