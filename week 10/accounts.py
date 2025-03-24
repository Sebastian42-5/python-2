# part 1

output_file = open('accounts.txt', 'w')

for _ in range(5):
    line = input('account info: ')

    output_file.write(line + '\n')

output_file.close()


# part 2

'''
from your accounts.txt, you're going to read each line and create a dictionary of dictionaries 
The outer dictionary key is the account number. The inner dictionary key is rhe last anmen and the 
valye is the balance. Print the created dictionary.

Ex: {account number : {lastname: balance}}


'''


