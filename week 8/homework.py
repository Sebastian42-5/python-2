'''
Firgus is behind on several assignments. After
rummaging through his backpack, he realizes that 
he has N items, each of which he records as strings. 
He has M upcoming assignments, the i-th of which requires 
Ti items to complete, r1, r2, ... rTi. If he has
all Ti required items, he can complete the i-th 
assignment. Otherwise, he flunks it. How many asssignments
can Firgus complete?

INPUT SPECIFICATION

--> first line contains 2 integers: N and M separated 
by a space


--> next N lines contains a single string si.
it is guaranteed that all strings will be unique


--> next M sections contain a single integer Ti, which is followed by Ti lines each containing a single string ri .


OUTPUT SPECIFICATION:

output a single integer on a single line, 
the answer to the problem (i.e the number of assignments Firgus can complete)

Sample input 
3 4 
chalk
cheese
charger
1
cheese
2
coins 
cash
3
charger 
chalk 
caffeine
3
cheese charger 
chalk 


A = {1, 2, 3, 4, 5, 6}

B = {2, 4, 6, 1}

B is a subset of A

Every element of B is in A

'''

def homework():

    N_and_M = input('Enter the number of items and assignments: ').split()

    homework_count = 0

    items = set()

    n = int(N_and_M[0])

    m = int(N_and_M[1])


    for i in range(n):
        items.add(input(f'Enter item number {i + 1}: '))
    
    for j in range(m):
        assignment = set()
        N_for_hw = int(input(f'Enter the number of items to complete the hw {j + 1}: '))
        for k in range(N_for_hw):
            assignment.add(input(f'Enter item {k + 1} for assignment {j + 1}: ') )
        if assignment.issubset(items):
            homework_count += 1

    print(homework_count)



homework()
