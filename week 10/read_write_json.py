import json

# deserialization of JSON => conversion of JSON object to its
# respective Python object

input_file = open('students.json', 'r')

data = json.load(input_file) # gives back a dictionary object 

print(data)



input_file.seek(0)

for line in input_file:
    print(line)

input_file.close()


# serialization of JSON => conversion of Python objects to JSON 
# objects/strings 

output_file = open('butterflies.json', 'w')

d = {'painted_lady': 1, 'bronze_copper': 12, 'monarch': 5}

json.dump(d, output_file, indent = 4)

output_file.close()