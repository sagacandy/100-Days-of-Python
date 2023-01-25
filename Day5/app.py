q1=input("What is the primary memory of a computer called? ")
a1=["RAM","ROM","Hard Drive","Processor"]
if q1==a1[0]:
    s1=1000
    print(f"Congratulations!! You have won Rs. {s1}")
else:
    s1=0
    print(f"Your answer is wrong, You have won Rs. {s1} ")
    
q2=input("Which of the following is not a type of software?")
a2=["Operating System", "Keyboard","Application","Firmware"]
if q2==a2[1]:
    s2=s1+1000
    print(f"Congratulations!! You have won Rs. {s2}")
else:
    s2=s1
    print(f"Your answer is wrong, You have won Rs. {s2} ")
q3=input("What is the full form of URL?")
a3=["Universal Resource Link", "Universal Resource Locator","Unique Resource Link","Unique Resource Locator"]
if q3==a3[1]:
    s3=s2+5000
    print(f"Congratulations!! You have won Rs. {s3}")
else:
    s3=s2
    print(f"Your answer is wrong, You have won Rs. {s3} ")

