# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''

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

# Question 3
'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''

# Question 4
'''
Using the json module write student information to the file in JSON format.  
That is, create a dictionary of of student data in the following format: 
gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}. 

Each dictionary in the list represents one student and contains the keys:
'first_name', 'last_name', 'exam1', 'exam2' and 'exam3'.  The keys map to the
values represengint each student's first name (string), last name (string) and 
three exam scores (integers).  

Output the gradebook_dict in JSON format to the file grades.json.  
'''

# Question 5
'''
Using the json module to read the grades.json file created in the previous
question.  Display the data in tabular format, including an additional 
column showing each student's average to the right of the student's three
exam grades and an additional row showing the class average on each exam.  
'''






from urllib.request import urlopen

def readFileURLString(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)

    return decoded_html

data_str = readFileURLString()

print()

output_fule = open('alice.txt', 'w', encoding = 'utf-8')


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
--> number of sentences
--> length of smallest and longest word, average length 
--> most common vowel
--> what is the average usage of punctuation marks for every 100 sentences


'''