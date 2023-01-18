# numbers=[]
# while True:
#     numbers=int(input("Enter the numbers to find avg: "))
#     if numbers=='done' or 'quit':
#         break
#     else:
#         numbers.append(numbers)
        
# print(numbers)



numbers=[]
while True:
    input_number=input("Enter the numbers to find average (or 'done' to quit): ")
    if input_number=='done':
        break
    else:
        numbers.append(int(input_number))

add_numbers=sum(numbers)
print('The sum of entered numbers is: ', add_numbers)
total_numbers=len(numbers)      #total number of terms
average=add_numbers/total_numbers
print(f'The average of Entered numbers {numbers} is: ', average)