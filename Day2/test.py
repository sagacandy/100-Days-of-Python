list=[2,4,3,5,6,7]
even=[]
odd=[]
for x in list:
  if x%2==0:
    even.append(int(x))
    # print(f'{x} is even')
  else:
    odd.append(int(x))
    # print(f"{x} is odd")
    
    
print("The even numbers are: ",even)
print("The odd numbers are: ",odd)
    