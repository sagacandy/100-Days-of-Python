user_input=input('Enter something: ')
try:
    value=int(user_input)
    print('You entered a number')
except:
    print('You entered string')