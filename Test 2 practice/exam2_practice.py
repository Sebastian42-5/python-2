# 2


# try: 

#     set1 = {3, 5, 12, 4} 

#     set2 = {5, 12, 2, 54} 

#     result = set1[0] 

# except TypeError: 

#     result = set1 and set2 

# print(result) 


# 3
  

# students_courses = { 

#     "Alice": {"Math", "Biology", "Chemistry"}, 

#     "Bob": {"Math", "English"}, 

#     "Charlie": {"Biology", "English"}, 

#     "Dana": {"Math", "Biology"}, 

# } 
 

# for student in students_courses: 

#     if "Math" in students_courses[student]: 

#         students_courses[student].remove("Math") 

  

# biology_students = {} 

# for student, courses in students_courses.items(): 

#     if "Biology" in courses: 

#         biology_students[student] = courses 

  

# print(biology_students) 



# 4



# class Tile:  

#     def __init__(self,interior:int):  

#         self.interior = [interior] 

#     def combine(self,other_tile): 
#         self.interior += other_tile.interior  
        
#     def __repr__(self): 
#         output = '' 
#         for item in self.interior: 
#             output += '[' + str(item) + ']' 
#         return output 
    
#     def __ge__(self, other_tile): 
#         output = True 
#         for i in range(len(self.interior)): 
#                 if i < other_tile.interior[i]: 
#                         output = False 
#         return output 

# tile_a = Tile(1)  

# tile_a.combine(Tile(2))  

# tile_b = Tile(3) 

# tile_b.combine(tile_a) 

# print(tile_a)  

# print(tile_b) 

# print(tile_a >= tile_b) 


# 4



# 5



# def endsWith(C, F):
#     ends = set()

#     try:
#         F = open(F, 'r')
#     except FileNotFoundError:
#         print('File not found.')
#         return None
#     else:
#         for line in F:
#             for word in line.split():
#                 if word.strip()[-1] == C:
#                     ends.add(word.strip())
#         F.close()
    
#     return ends

# print(endsWith('t', 'sharks.txt'))


# 6 

# from __future__ import annotations

# class Car:
#     def __init__(self, brand = 'Toyota', year = 2025, fuel_level = 100):
#         self.brand = brand
#         self.year = year
#         self.fuel_level = fuel_level
    
#     def __repr__(self):
#         return '[' + self.brand + str(self.year) + str(self.fuel_level) + ']'
    
#     def refuel(self, fuel: int) -> None:
#         self.fuel_level += fuel
#         if self.fuel_level > 100:
#             self.fuel_level = 100
    
#     def drive(self, distance: int) -> tuple:
#         self.fuel_level -= distance 
#         if self.fuel_level < 0:
#             self.fuel_level = 0 
        
#         return (self.fuel_level, distance)
    
#     def __lt__(self, other_car: Car) -> bool:
#         return isinstance(other_car, Car) and self.year < other_car.year
    



# my_car = Car()

# my_car.refuel(30)

# print(my_car.drive(30))


# print(my_car)

# car_2 = Car(brand = 'Ford', year = 2023, fuel_level = 90)

# print(my_car < car_2)


# 7 



# d = {'a': {'b': {'c': 42}}} 

# d['a']['b']['c'] = set('Hello')  

# print(d)  

# 8 



# def compare(n): 

#     return len(n) != len(set(n))  

# print(compare([1, 2, 3, 4])) 

# print(compare([1, 2, 2, 3])) 


# 9)   

# What is the purpose of the “finally” block in Python exceptions? 

  

# A) It executes only if an exception occurs.   

# B) It executes only if no exception occurs.   

# C) It executes only when a specific exception is raised.   

# D) It always executes, regardless of whether an exception occurs or not. 

# 10 

# users = { "alice": { "age": 25, "favorites": { "color": "blue", "fruit": "mango" } }, "carol": { "age": 22, "favorites": { "color": "purple"} } } 

# for user in users:
#     if 'fruit' in users[user]['favorites']:
#         print(users[user]['favorites']['fruit'])



# 11


# data = { 

#     "students": { 

#         "Alice": {"Math", "English"}, 

#         "Bob": {"Math", "History"}, 

#         "Charlie": {"History", "English"} 

#     } 

# } 

  

# data["students"]["Bob"].add("Science") 

  

# data["students"]["Alice"].discard("English") 

  

# all_subjects = set() 

# for subjects in data["students"].values(): 

#     all_subjects.update(subjects) 

  

# print(len(all_subjects)) 


# 12


"""You are given a dictionary of peoples' objects, where the key is the name of the person and the 

corresponding value is the dictionary of the things they own. You are to determine who of the people in the lists has the  

greatest number of objects, counting the fact that each person can have friends and therefore access to their friends extra objects,  

they need to leave at least one object of each type to their friend. 

 

example: 

input: 

d={"John":{"calculator":5,"gums":7,"phones":2,"bike":1}, 

"Anna":{"boats":5,"pencils":9}, 

"Robert":{"friends":["Anna"],"pairs of shoes":2}}#Assume for semplicity you can only name friends that are in the dictionary before the stated person 

 

output: 

"John" 

15 

 

""" 




# def compute_total_objects(person, data):
#     total = 0 

#     for item, count in data[person].items():
#         if item != 'friends':
#             total += count
    
#     if 'friends' in data[person]:
#         for friend in data[person]['friends']:
#             for item, count in data[friend].items():
#                 if item != 'friends' and count >= 1:
#                     total += 1
    
#     return total 



# d = {"John":{"calculator":2,"gums":3,"phones":2,"bike":1}, 

# "Anna":{"boats":5,"pencils":2, "airplanes": 1, "bazookas": 1, "knights": 1}, 

# "Robert":{"friends":["Anna"],"pairs of shoes":6}}


# max_object = 0 

# max_person = ''


# for person in d:
#     total = compute_total_objects(person, d)

#     if total > max_object:
#         max_object = total 
#         max_person = person


# print(max_person)

# print(max_object)



# 13





# 14

# def Convertion(val):
#     if type(val) == str:
#         return int('val')
#     return 'safe'


# try:
#     result = Convertion('abc')
#     print(f'Converted: {result}')

# except TypeError:
#     print('TypeError occured')

# except ValueError:
#     print('ValueError occured')

# else:
#     print('No error')

# finally:
#     print('Done')

# Here, it is Value Error, bc it's trying to turn a str with letters into an int.



# 15 


# def divide_numbers(a, b): 

#     try: 

#         result = a / b 

#     except ZeroDivisionError: 

#         return "Cannot divide by zero." 

#     except TypeError: 

#         return "Invalid input types." 

#     else: 

#         return f"Result is {result}" 
    
# print(divide_numbers('10', '2'))

    
# 17 



# 19 


# 20 

# B)


# 21


def operation():
    try:
        numbers = [10, 0, 'a']

        for i in range(len(numbers)):
            print(100 // numbers[i])

    except ZeroDivisionError:
        print('You cannot divide by zero')
    
    except TypeError:
        print('Invalide type')
    
    finally:
        print('execution completed')


operation()

# it doesn't try for all values in numbers, it tries one by one and if it suceeeds, it will print it. 









            
