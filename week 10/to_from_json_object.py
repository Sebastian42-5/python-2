import json 

# convert from JSON to Python 

student_record = '{"name": "Lucy", "year": 1, "college": "Dawson"}'

parsed_record = json.loads(student_record)  # parse (translate) student record to python

# print(parsed_record)

# print(type(parsed_record))

# convert from python to JSON

student_dict = {'name': 'Lucy', 'year': 1, 'college': 'Dawson'}

student_record_json = json.dumps(student_dict)

print(student_record_json)


print('\n\n')

print(json.dumps({'name': 'Lucy', 'year': 1})) 

print('\n')

print(json.dumps(['red', 'green', 'blue']))

print(json.dumps(('apples', [1, 2, 3])))   # in JSON it's arrays for both lists and tuples. Ther is no distinction. 

print(json.dumps('Hello World!'))

print(json.dumps(12.33))
print(json.dumps(12))

print(json.dumps(True))  # True --> true
print(json.dumps(False)) # False --> false
print(json.dumps(None)) # None --> null

# .loads() takes a str

# print(json.loads(str(12)))
# print(json.loads(str(12.33)))



