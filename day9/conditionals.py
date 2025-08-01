#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int (input("enter your age:"))
if age >= 18 :
    print("You are old enough to drive")
else:
    print("wait for the missing amount of years")
#Compare the values of my_age and your_age using if ... else. Who is older me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = 25
your_age = int (input("enter your age :"))
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am older than you by 1 year")
    else:
        print(f"I am older than you by {age_diff} years")
else:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are older than me by 1 year")
    else:
        print(f"You are older than me by {age_diff} years")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#level 2
#1. Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

score = int(input("Enter your score: "))
if 80 <= score and score <= 100:
    print("Grade: A")
elif 70 <= score and score< 80:
    print("Grade: B")
elif 60 <= score and score < 70:
    print("Grade: C")
elif 50 <= score and score < 60:
    print("Grade: D")   
else:
    print("Grade: F")

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season = str(input("Enter the month: "))
if season in ["september", "october", "november"]:
    print("The season is Autumn")
elif season in ["december", "january", "february"]:
    print("The season is Winter")
elif season in ["march", "april", "may"]:
    print("The season is Spring")
elif season in ["june", "july", "august"]:
    print("The season is Summer")
else:
    print("Invalid month entered")
#3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list
#and print the modified list. If the fruit exists print('That
#fruit already exist in the list')

fruit_to_check = input("Enter a fruit to check: ")
if fruit_to_check in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit_to_check)
    print("Modified list:", fruits)

#level 3
#1. Here we have a person dictionary.
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB',
'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}
''' *Check if the person dictionary has skills key, if so print
out the middle skill in the skills list.
* Check if the person dictionary has skills key, if so check
if the person has 'Python' skill and print out the result.
* If a person skills has only JavaScript and React, print('He
is a front end developer'), if the person skills has Node,
Python, MongoDB, print('He is a backend developer'), if the
person skills has React, Node and MongoDB, Print('He is a
fullstack developer'), else print('unknown title') - for more
accurate results more conditions can be nested!
* If the person is married and if he lives in Finland, print
the information in the following format: '''

if 'skills' in person:
    skills = person['skills']
    print("Middle skill:", skills[len(skills) // 2])
    
    if 'Python' in skills:
        print("The person has Python skill")
    
    if 'JavaScript' in skills and 'React' in skills :
        print("He is a front end developer")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

        