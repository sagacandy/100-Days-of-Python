def favg (a,b):
    avg=(a+b)/2
    print('The average is: ', avg)
    
try:
    a=int(input("Enter the fist number: "))
    b=int(input("Enter the fist number: "))
    favg(a,b)
except:
    print("Invalid input")