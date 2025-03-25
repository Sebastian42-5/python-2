# part 1

output_file = open('accounts.txt', 'w')

for _ in range(5):
    line = input('account info: ')

    output_file.write(line + '\n')

output_file.close()


# part 2

'''
from your accounts.txt, you're going to read each line and create a dictionary of dictionaries 
The outer dictionary key is the account number. The inner dictionary key is the last name and the 
value is the balance. Print the created dictionary.

Ex: {account number : {lastname: balance}}


'''

input_file = open('accounts.txt', 'r')

result_dict = {}

for line in input_file: 
    account_number, lastname, balance = line.split()

    if account_number not in result_dict:
        result_dict[account_number] = {}

        if lastname not in result_dict[account_number]:
            result_dict[account_number][lastname] = balance

print(result_dict)





