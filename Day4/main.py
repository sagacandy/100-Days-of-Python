def func():
    try:  
        l=[1,3,5,7]
        i = int(input("Enter the index number: "))
        print(l[i])
        return 1
    except:
        print("Please input valid index range")
        return 0
    finally:
        l.close()
        
x=func()
print(x)