#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1 = 'thirty'
string2= 'days'
string3= 'of'
strings4= 'python'
print(string1 +' '+ string2 +' ' + string3 +' '+ strings4)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

word1 = 'Coding'
word2 = 'For'
word3 = 'All'
print(word1 + ' '+ word2 +' '+ word3 ) 

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4. Print the variable company using print().

print(company)

#5. Print the length of the company string using len() method and print().
length = len(company)
print(length)

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
print(company[6:])

#10. Check if Coding For All string contains a word Coding using the method index,find or other methods.
print(company.find('Coding'))

#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'python'))

#12. Change Python for Everyone to Python for All using the replace method or other methods.
phrase = 'Python for Everyone'
new_phrase = phrase.replace('Everyone', 'All')
print(new_phrase)

#13.Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_name = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_name.split(','))

#15.What is the character at index 0 in the string Coding For All.
print(company[0])
#16.What is the last index of the string Coding For All.
print(len(company) - 1)

#17. What character is at index 10 in 'Coding For All' string.
print(company[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"
words = phrase.split()           
a, b, c = words                  
acronym = a[0] + b[0] + c[0]     
print(acronym)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
phrase = "Coding For All" 
words = phrase.split()
a, b, c = words
acronym = a[0] + b[0] + c[0]
print(acronym)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All.
print(company.rfind('l'))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#24. Use rindex to determine the position of the last occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25.Slice out the phrase 'because because because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
phrase = sentence[start:end]
print(phrase)

#26.Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

28.# Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#29. Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#30. Create a string '   Coding For All      ' and remove the leading and trailing spaces.
string_with_spaces = '   Coding For All      '
trimmed_string = string_with_spaces.strip()
print(trimmed_string)

#31.Which one of the following variables return True when we use the method isidentifier():
#    o 30DaysOfPython
#    o thirty_days_of_python
is_identifier1 = '30DaysOfPython'
is_identifier2 = 'thirty_days_of_python'    
print(is_identifier1.isidentifier())  
print(is_identifier2.isidentifier())  

32.#The following list contains the names of some of python libraries: ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_libraries))

#33. Use the new line escape sequence to separate the following sentences.
sentence1 = "I am enjoying this challenge"
sentence2 = "I just wonder what is next"
print(sentence1 + '\n' + sentence2)

#34. Use a tab escape sequence to separate the following sentences.
#Name Age Country City
#Asabeneh 250 Finland Helsinki
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

#35. Use the string formatting method format() to format the following sentences.
radius = 10 
area_of_circle = 3.14 * radius ** 2
print("The area of a circle with a radius {} is {:.2f} meters square.".format(radius, area_of_circle))

#36. Make the following using string formatting methods:
a = 8
b = 6
print((f"{a} + {b} = {a + b}"))
print((f"{a} - {b} = {a - b}")) 
print((f"{a} * {b} = {a * b}"))
print((f"{a} / {b} = {a / b:.2f}"))
print((f"{a} % {b} = {a % b}"))
print((f"{a} // {b} = {a // b}"))
print((f"{a} ** {b} = {a ** b}"))          
