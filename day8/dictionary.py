#1. Create an empty dictionary called dog
dog ={}

#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'bidu'
dog['color'] = 'white'
dog['breed'] = 'labrador'
dog['legs'] = 4
dog['age'] = 5
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age,marital status, skills, country, city and address as keys for the dictionary
student_dict = {}

student_dict['first_name'] = 'John'
student_dict['last_name'] = 'Doe'
student_dict['gender'] = 'male'
student_dict['age'] = 20
student_dict['marital_status'] = 'single'
student_dict['skills'] = ['python', 'java', 'c++']
student_dict['country'] = 'usa'
student_dict['city'] = 'new york'
student_dict['address'] = '123 main st'
print(student_dict)

#4. Get the length of the student dictionary
print('Length of student dictionary:', len(student_dict))

#5. Get the value of skills and check the data type, it should be a list
print('Skills:', student_dict['skills'])
print('Data type of skills:', type(student_dict['skills']))

#6. Modify the skills values by adding one or two skills
student_dict['skills'] = ['sql','javascript']
print('Updated Skills:', student_dict['skills'])

#7. Get the dictionary keys as a list
student_keys = list(student_dict.keys())
print(student_keys)

#8. Get the dictionary values as a list
student_values = list(student_dict.values())
print(student_values)

#9. Change the dictionary to a list of tuples using items() method
print(student_dict.items())

#10. Delete one of the items in the dictionary
print(student_dict.pop('age'))

#11. Delete one of the dictionaries
dic = dict(student_dict)
del student_dict

