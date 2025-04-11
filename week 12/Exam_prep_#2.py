'''
You are a backyard fence constructor and you have 4 costumers in your waiting list.

The waiting list is a nested dictionary where the outer keys are the names of the five people in the waiting list (str), 
the inner keys are the dollar bills that each person has (int) and the values of those inner keys are the amount of bills of that type (int)

There will be 10, 20, 50, and 100 dollar bills allowed.

Every square meter of fence enclosure for the backyard costs 15 dollars per square meter. 

Each person will pay and if there is change, that is what the person will have left on their account.

That means that you have to update the dictionary after they paid.

Once they paid, you have to build the enclosure for each person.

On a txt file called fences.txt , you are going to print the name of the person, an empty line, and the enlcosure that is constructed by '_' and '|'

and where a square meter is like this:
 _
|_|

Here is the information for each person:

{'Jessica': {10: 5, 20: 6, 50: 2, 100: 0}, 
 'Bob': {10: 8, 20: 7, 50: 1, 100: 1}, 
 'Kevin': 10: 5, 20: 4, 50: 3, 100: 2, 
 'Lea': 10: 9, 20: 3, 50: 0, 100: 3} } 

The result will be the txt file and the change for each person after they pay for the enclosure. 


'''


waiting_lst = {'Jessica': {10: 5, 20: 6, 50: 2, 100: 0}, 
 'Bob': {10: 8, 20: 7, 50: 1, 100: 1}, 
 'Kevin': {10: 5, 20: 4, 50: 3, 100: 2}, 
 'Lea': {10: 9, 20: 3, 50: 0, 100: 3} } 

print(waiting_lst)

