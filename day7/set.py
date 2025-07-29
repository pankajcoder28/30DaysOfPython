# level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Find the length of the set it_companies
print('length of it_compnies : ',len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(('tesla','scs','cisco','bookmyshow','netflix'))
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove('netflix')
print(it_companies)

#5. What is the difference between remove and discard
it_companies.discard('pankaj') # discard does not raise an error if the item is not found, while remove raises a KeyError
#it_companies.remove() # remove raises KeyError if the item is not found

#level 2

#1. Join A with B
c = A.union(B)
print(c)

#2. Find A intersection B
print(A.intersection(B))

#3. Is A subset of B
print(A.issubset(B))

#4. Are A and B disjoint sets
print(A.isdisjoint(B))

# 5. Join A with B and B with A
d = A.union(B)  
e = B.union(A)
print(d)
print(e)

#6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7. Delete the sets completely
del A
del B

#level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)
print('length of age list :',len(age))
print('length of age set :',len(age_set))
print(age == age_set)

#2. Explain the difference between the following data types: string, list, tuple and set
# String: A string is a sequence of characters enclosed in quotes. It is immutable, meaning it cannot be changed after creation.
# List: A list is an ordered collection of items that can be changed (mutable). It can contain duplicate items and is defined using square brackets.
# Tuple: A tuple is similar to a list but is immutable, meaning it cannot be changed after creation. It is defined using parentheses.
# Set: A set is an unordered collection of unique items. It does not allow duplicate items and is defined using curly braces. Sets are mutable, but the items within a set must be immutable (e.g., numbers, strings, tuples).

#3.I am a teacher and I love to inspire and teach people. How many unique
#words have been used in the sentence? Use the split methods and set to get
#the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
uniqe_words = set(sentence.split())
print('Unique words in the sentence:', uniqe_words)