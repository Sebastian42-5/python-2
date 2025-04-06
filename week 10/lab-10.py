# PART 1


# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''

# from collections import Counter

input_file = open('sharks.txt', 'r', encoding = 'UTF8')

shark_content = input_file.read().rstrip()

# print(shark_content)

# print('\n')

shark_lst = shark_content.split()

word_count = len(shark_lst)

frequency_dict = {}



def word_frequency_count(lst):

    frequency_dict = {}

    for word in shark_lst:

        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict



# print(word_frequency_count(frequency_dict))

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


# print(' '.join(sorted_words))


# print('\n')




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



# PART 2


# Question 4
'''
Using the json module write student information to the file in JSON format.  
That is, create a dictionary of of student data in the following format: 
gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}. 

Each dictionary in the list represents one student and contains the keys:
'first_name', 'last_name', 'exam1', 'exam2' and 'exam3'.  The keys map to the
values representing each student's first name (string), last name (string) and 
three exam scores (integers).  

Output the gradebook_dict in JSON format to the file grades.json.  
'''

import json 

gradebook_dict = {'students': \
[{'first_name': 'Loic', 'last_name': 'Nzenang', 'exam1': 100, 'exam2': 90, 'exam3': 98},\
{'first_name': 'Joey', 'last_name': 'Meyo', 'exam1': 95, 'exam2': 94, 'exam3': 87},\
{'first_name': 'Maya', 'last_name': 'Gonzalez', 'exam1': 89, 'exam2': 95, 'exam3': 76},\
{'first_name': 'Miko', 'last_name': 'Semi', 'exam1': 76, 'exam2': 70, 'exam3': 84},\
{'first_name': 'Hyou', 'last_name': 'Fei', 'exam1': 67, 'exam2': 90, 'exam3': 98}\
]}
# gradebook_dict = {'firstname': {'year': 1}}

output = open('grades.json', 'w')


json.dump(gradebook_dict, output)

output.close()


# Question 5
'''
Using the json module to read the grades.json file created in the previous
question.  Display the data in tabular format, including an additional 
column showing each student's average to the right of the student's three
exam grades and an additional row showing the class average on each exam.  
'''

input = open('grades.json', 'r')

grades_dict = json.load(input)

exam1total, exam2total, exam3total = 0, 0, 0

for student in grades_dict['students']:
    average = (student['exam1'] + student['exam2'] + student['exam3']) // 3

    student['average'] = average


    exam1total += student['exam1']
    exam2total += student['exam2']
    exam3total += student['exam3']

exam1_avg = exam1total / len(gradebook_dict['students'])
exam2_avg = exam2total / len(gradebook_dict['students'])
exam3_avg = exam3total / len(gradebook_dict['students'])

# for student in grades_dict['students']:
#     print(student['first_name'], student['last_name'], student['exam1'], student['exam2'], student['exam3'], student['average'])

# print(exam1_avg, exam2_avg, exam3_avg)




# extra question:



'''
--> pick 5 books
--> read 4 of the 5 books
--> write each of the 4 books into a separate file, automate this process as much as possible 
--> The fifth book title keep in mind, but don't read/write it

using try-except block to do the following:

--> read number of words of the story only
--> find the frequency of each word in the file
--> number of paragraphs
--> number of sentences
--> length of smallest and longest word, average length 
--> most common vowel
--> what is the average usage of punctuation marks for every 100 sentences


'''



from urllib.request import urlopen

def readFileURLString(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)

    return decoded_html


url_list = ['https://gutenberg.org/cache/epub/174/pg174.txt', 'https://gutenberg.org/cache/epub/64317/pg64317.txt', \
            'https://gutenberg.org/cache/epub/2701/pg2701.txt', 'https://gutenberg.org/cache/epub/16389/pg16389.txt', \
                'https://gutenberg.org/cache/epub/2554/pg2554.txt']



for i in range(len(url_list) - 1):

    data_str_url = readFileURLString(url_list[i])

    output_file = open(f'book{i + 1}.txt', 'w', encoding = 'utf-8')

    output_file.writelines(data_str_url)

    output_file.close()



for j in range(len(url_list) - 1):

    input_file = open(f'book{j + 1}.txt', 'r', encoding = 'utf-8')

    all_words = input_file.read()

    word_lst = all_words.split()

    number_of_words = len(word_lst)

    print(number_of_words)

    print(word_frequency_count(all_words))

    # count the number of paragraphs

    parts = all_words.split('\n\n')

    paragraph_count = 0

    for part in parts:
        if part.strip():
            paragraph_count += 1
    
    print(paragraph_count)

    # number of sentences

    book_str = ''.join(word_lst)

    print(book_str.count('.'))

    # length of smallest and longest word, average length




















# print()

# output_file = open('alice.txt', 'w', encoding = 'utf-8')
