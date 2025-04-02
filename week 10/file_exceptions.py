file_name = 'book.txt'

try:

    input_file = open(file_name, 'r')

except FileNotFoundError:
    print(f'Sorry, the file {file_name} does not exist')
    output_file = open(file_name, 'w', encoding = 'UTF8')
    # pass

else:

    for line in input_file:
        print(line.rstrip())




'''
1) Count the number of words





2) Make two files: cats.txt and dogs.txt. Store at least three names of cats in the first 
file and three names of dogs in the second file. Write a program that tries to read these files
and print the contents of the file to the screen. Wrap your code in a try except block to catch 
the FileNotFoundError , and print a friendly message if a file is missing. Move one of the files to a different location on 
your system, and make sure that the code in the except block executes proper



3) modify your previous code to fail silently if either file is missing 

4) One common problem when prompting for numerical input occurs when providing 
text instead of number. In such case, when trying to convert the input to int, a ValueError occurs. Write a program 
that prompts the user for two numbers, add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your program by entering two 
numbers and then by entering some text instead of a number.

'''

# 1)

# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''





input_file = open('sharks.txt', 'r', encoding = 'UTF8')

shark_content = input_file.read()

shark_lst = shark_content.split()

word_count = len(shark_lst)

# output_file.writelines(shark_lst)




print(word_count)



input_file.close()
# output_file.close()







# 2) 

dog_names = ['Albert ', 'Cupcake ', 'Winston ']

cat_names = ['Destructor ', 'Terminator ', 'Ruler ']


dog_file = open('dog.txt', 'w')
cat_file = open('cat.txt', 'w')


dog_file.writelines(dog_names)
cat_file.writelines(cat_names)

dog_file.close()
cat_file.close()


try:

    dog_input = open('cats.txt', 'r')
    cat_input = open('dog.txt', 'r')

except FileNotFoundError:
    print('One of the files does not exist.')

else:
    for line in dog_input:
        print(line.rstrip())
    for line in cat_input:
        print(line.rstrip())


    dog_input.close()
    cat_input.close()



# 3) 

# I would change the print message under the except to a pass for my code to fail silently.

# 4) 



answer = input('You want to add to numbers or not? ')

if answer == 'yes':

    while True:
        try:
            num1 = int(input('Enter the first number to be added: '))
            num2 = int(input('Enter the second number to be added: '))
        
        except ValueError:
            print('One of your numbers is not an integer. Try again!')

        else:
            print(num1 + num2)
            break

else:
    print('I guess next time...')    



