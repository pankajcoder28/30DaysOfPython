# level 1

#1. Create an empty tuple
tpl = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are acceptable)
bro = ('tarun','rio','ankur','ankit')
sis = ('priya','pooja','jolly')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = bro + sis
print("siblings :", siblings)

# 4. How many siblings do you have?
print("i have %d siblings" %len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('gangadhar','tapaswini')
print(family_members)

#level 2

#1. Unpack siblings and parents from family_members
print("parents :", family_members[-2:])
print('siblings :', family_members[0:-2])

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Milk', 'Eggs', 'Cheese', 'Yogurt')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print("middle item : ",food_stuff_lt[6:7])

#5. Slice out the first three items and the last three items from food_staff_lt list
print("First three items:", food_stuff_lt[:3])
print("Last three items:", food_stuff_lt[-3:])

#6. Delete the food_stuff_lt list completely
del food_stuff_lt

#7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway',
'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
