numbers = []
while True:
    input_number = input(
        "Enter the numbers to find average (or 'done' to quit): ")
    if input_number == 'done':
        break
    else:
        try:
            numbers.append(int(input_number))
        except:
            print("Invlaid input!!!")

add_numbers = sum(numbers)  # sum of entered numbers
print('The sum of entered numbers is: ', add_numbers)
total_numbers = len(numbers)  # total number of terms
average = add_numbers/total_numbers  # average of entered numbers
print(f'The average of Entered numbers {numbers} is: ', average)
