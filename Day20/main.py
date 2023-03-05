# x = 0
# match x:
#     case 0:
#         print("The number is zero")
#     case 5:
#         print("the number is 5")
#     case _:
#         print(f"case 3 the number is {x}")


# to find if the person is adult or tenage or old or children
age = int(input("Enter your age: "))
match age:
    case age if age <= 10:
        print("You are Children")
    case age if age > 10 and age <= 20:
        print("You are teenage")
    case age if age > 20 and age <= 40:
        print("You are adult")
    case _:
        print("You are old")
