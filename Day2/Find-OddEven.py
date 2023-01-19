list=[]
even=[]
odd=[]
while True:
    input_numbers=input("Enter the number or ('done' to quit): ")
    if input_numbers=='done':
        break
    else:
        list.append(int(input_numbers))
print(f"The given numbers are {list}")

#code to find even or odd
for x in list:
  if x%2==0:
    even.append(int(x))
    # print(f'{x} is even')
  else:
    odd.append(int(x))
    # print(f"{x} is odd")

print("The even numbers are: ",even)
print("The odd numbers are: ",odd)
    
