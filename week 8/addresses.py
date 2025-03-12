'''
There are many ways to write e-mail addresses. 

--> take a gmail address and add a + and a string before @ symbol and e-mail is still valid

Examples:

lousia.harutyunyan@gmail.com

louisa.harutyunyan+helloworld@gmail.com


--> dots before the @ symbol are also ignored.

sebassotosandrea@gmail.com

sebas.so.t.o.s.a.n.d.r.e.a@gmail.com

--> uppercase and lowercase differences throughout the addresses are also ignored.

Examples

sebassotosandrea@gmail.com

sebaSsOtOsAndReA@gMaIL.com



Given email addresses, determine the number of them that are unique.

The rules for email addresses are the same as above


Input specification:

you use lists, 

--> first line of input is integer n
designating number of email addresses to read, 

--> the next n lines are the n addresses. 

Output:

characters before the at symbol can be +, characters 

At least one before the at 

The user is going to put the correct output


Sample input 

foo@bar.com
fO.o+bax123@bar.com

fOo@bar.com

'''

def clean(email_address: str):

    email_address = email_address.lower()

    plus_index = email_address.find('+')

    at_index = email_address.find('@')

    # if it doesn't find the +, it will return -1

    if plus_index != -1:
        email_address = email_address[:plus_index] + email_address[at_index:]

    # remove all dots

    email_address = email_address.replace('.', '')


    return email_address 



# main program


n = int(input('Enter the number of emails to read: '))

addresses = {}

for i in range(n):
    email_address = input(f'Enter the email {i + 1}: ')

    email_address = clean(email_address)

    addresses.add(email_address)


print(len(addresses))




# sets

# unordered unique elements 

# the elements have to be immutable

# {12, 33 72, 77}

# it prints {72, 33, 12, 77}

# sets are faster than lists, because they are sorted with hashs

# {11, 33, 72} == {33, 11, 72} -> True

# {11, 11, 33, 72} == {33, 11, 72}

# len({11, 12}) -> 2

# a {} is an empty dict not an empty set 

# set = set({})

# you cannot index through elements of a set 

# {(1, 2), (3, 5)} this is fine

# {(1, 2), (2, 3, [4, 5]), (3, 4)}  this is problematic because it contains a list, a mutable object 

# in a set you do searching in a constant time, in a list you do searching in linear time 

# A set works with hash tables 4, 5, 6 (constant index access) 

# functions

# s.add(2) (it adds it somewhere)

# s.remove(33)

# 5 in s -> false

# s1 = {1, 2, 3, 4}
# s2 = {5, 6, 7, 8, 9}

# s1.update(s2) s2 doesn't change but s1 is gonna be extended with s2

# s1 becomes {1, 2, 3, 4, 5, 6, 7, 8, 9}
# s2 is {5, 6, 7, 8, 9}

# dir(set())

# dir('')

# help(set().union())  -> return the union of sets as a copy of the set 














    