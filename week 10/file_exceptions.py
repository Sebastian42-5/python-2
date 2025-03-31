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

input_file = open('sharks.txt', 'r', encoding = 'UTF8')

shark_lst = input_file.readlines()
output_file.writelines(shark_lst)

input_file.close()
output_file.close()


'''
1) Count the number of files 

2) Make two files: cats.txt and dogs.txt. Store at least three names of cats in the first 
file and three names of dogs in the second file. Write a program that tries to read these files
and print the contents of the file to the screem. Wrap your code in a try except block to catch 
the FileNotFoundError , and print a friendly message if a file is missing. Move one of the files to a different location on 
your system, and make sure that the code in the except block executes proper


3) modify your previous code to fail silently if either file is missing 

4) One common problem when promting for numerical input occurs when providing 
text instead of number. In such case, when trying to convert the input to int, a ValueError occurs. Write a program 
that prompts the user for two numbers, add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your program by entering two 
numbers and then by entering some text instead of a number.

'''



