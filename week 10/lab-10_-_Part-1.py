# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequency from highest to lowest. Display the results.
'''
# from collections import Counter

input_file = open('sharks.txt', 'r', encoding = 'UTF8')

shark_content = input_file.read().rstrip()

print(shark_content)

print('\n')


shark_lst = shark_content.split()

word_count = len(shark_lst)

frequency_dict = {}

for word in shark_lst:

    if word not in frequency_dict:
        frequency_dict[word] = 1
    else:
        frequency_dict[word] += 1


# print(frequency_dict)

# print('\n')


word_frequency = []

for word, count in frequency_dict.items():
    word_frequency.append((count, word))

# replace this with a bubble sort or another sorting algorithm

word_frequency = sorted(word_frequency)[::-1]

sorted_words = []

for count, word in word_frequency:
    for _ in range(count):
        sorted_words.append(word)


print(' '.join(sorted_words))


print('\n')




# output_file.writelines(shark_lst)

# word_frequency = Counter(shark_lst)

# print(word_frequency)



print(f'Your story has: {word_count} words')



input_file.close()
# output_file.close()





# Question 2
'''
Make two files: cats.txt and dogs.txt.  Store at least three names of cats in the first
file and three names of dogs in the second file.  Write a program that tries to read
these files and print the contents of each file to the screen.  

(a) Wrap your code in a try-except block to catch the FileNotFoundError and print a 
    friendly message if a file is missing.  To test your code, move one of the files 
    to a different location on your system, and make sure that the code in the except 
    block executes properly.  
(b) Modify your previous code to fail silently if either file is missing
'''

# This code has already been done 

# dog_names = ['Albert ', 'Cupcake ', 'Winston ']

# cat_names = ['Destructor ', 'Terminator ', 'Ruler ']


# dog_file = open('dog.txt', 'w')
# cat_file = open('cat.txt', 'w')


# dog_file.writelines(dog_names)
# cat_file.writelines(cat_names)

# dog_file.close()
# cat_file.close()


# try:

#     dog_input = open('cats.txt', 'r')
#     cat_input = open('dog.txt', 'r')

# except FileNotFoundError:
#     print('One of the files does not exist.')

# else:
#     for line in dog_input:
#         print(line.rstrip())
#     for line in cat_input:
#         print(line.rstrip())


#     dog_input.close()
#     cat_input.close()



# 3) 


# dog_names = ['Albert ', 'Cupcake ', 'Winston ']

# cat_names = ['Destructor ', 'Terminator ', 'Ruler ']


# dog_file = open('dog.txt', 'w')
# cat_file = open('cat.txt', 'w')


# dog_file.writelines(dog_names)
# cat_file.writelines(cat_names)

# dog_file.close()
# cat_file.close()


# try:

#     dog_input = open('cats.txt', 'r')
#     cat_input = open('dog.txt', 'r')

# except FileNotFoundError:
#     pass

# else:
#     for line in dog_input:
#         print(line.rstrip())
#     for line in cat_input:
#         print(line.rstrip())


#     dog_input.close()
#     cat_input.close()


# I would change the print message under the except to a pass for my code to fail silently.

# Question 3
'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''

# This code has already been done 



# while True:
#     try:
#         num1 = int(input('Enter the first number to be added: '))
#         num2 = int(input('Enter the second number to be added: '))
    
#     except ValueError:
#         print('One of your numbers is not an integer. Try again!')

#     else:
#         print(num1 + num2)
#         break



