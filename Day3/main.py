try:
    num=int(input("Enter the number: "))
    print(f"The multiplication table of {num} is :")
except:
    print("Invlaid Input!! Please enter integer")
try:
    for i in range(1,11):
        print(f"{num} X {i} = ", num*i)
        
except:
    print("This will not run unless you enter integer")
     
     