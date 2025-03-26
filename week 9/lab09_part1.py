# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value in 
the inner dictionary is the balance.  Print the final dictionary.  
'''


# input_file = open('accounts.txt', 'r')

# result_dict = {}

# for line in input_file: 
#     account_number, lastname, balance = line.split()

#     if account_number not in result_dict:
#         result_dict[account_number] = {}

#         if lastname not in result_dict[account_number]:
#             result_dict[account_number][lastname] = balance

# print(result_dict)


# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

(b) Once your grades.txt file is populated, read and store the information
    from the file.  Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''

# part a) 

output_file = open('grades.txt', 'w')

n = int(input('Enter the number of students: '))

for i in range(n):
    line = input(f'Enter grade info for student {i + 1}: ')

    output_file.write(line + '\n')

output_file.close()

# part b) 

input_file = open('grades.txt', 'r')

grade_dict = {}

each_line = line.split()

for each_line in input_file:

    each_line = each_line.split()

    key = (each_line[0], each_line[1])

    value_lst = each_line[2:]

    # print(value_lst)

    value = list(map(int, value_lst))

    grade_dict[key] = value

input_file.close()


average_lst = []

exam1_lst = []

exam2_lst = []

exam3_lst = []


for key in grade_dict:
    max_value = max(grade_dict[key])

    min_value = min(grade_dict[key])

    average = sum(grade_dict[key]) / len(grade_dict[key])

    average_lst.append(average)

    exam1_lst.append(grade_dict[key][0])

    exam2_lst.append(grade_dict[key][1])

    exam3_lst.append(grade_dict[key][2])

    print(f'\nFor {' '.join(key)}, the max value is : {max_value}, the min value is: {min_value}, and the average is : {average}')


all_min_max = [min(exam1_lst), max(exam1_lst), min(exam2_lst), max(exam2_lst), min(exam3_lst), max(exam3_lst)]


overall_average = sum(average_lst) / len(average_lst)


print(f'\nThese are the min and max values for each exam for all students, respectively: {all_min_max}')

print(f'\nThe overall average across all the grades of all the students is : {overall_average}')



    
















