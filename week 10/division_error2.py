print('You are two enter two numbers, which I will divide for you')
print('Enter \'q\' to quit any time. ')

while True:
    first_number = input('\n First number: ')
    if first_number == 'q':
        break

    second_number = input('Second number: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number) / int(second_number)
    
    except ZeroDivisionError:
        print('You cannot divide by zero')
    
    else:  # execute if try block succeeds

        print(f'The result is {result}')