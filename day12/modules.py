#level 1
#1. Writ a function which generates a six digit/character random_user_id.
import random
import string
def generate_user_id():
    allowed_chars = string.ascii_letters + string.digits
    user_id = ''
    for i in range(6):
        user_id += random.choice(allowed_chars)
        
    return user_id

print(generate_user_id())

'''2. Modify the previous task. Declare a function named user_id_gen_by_user. It
doesn’t take any parameters but it takes two inputs using input(). One of the
inputs is the number of characters and the second input is the number of IDs
which are supposed to be generated.'''
import string
def user_id_gen_by_user():
    num_of_chars = int(input("Enter the number of characters for user ID: "))
    num_of_ids = int(input("Enter the number of IDs to generate: "))
    allowed_chars = string.ascii_letters + string.digits

    for i in range(num_of_ids):
        one_id = ''
        for j in range(num_of_chars):
            one_id += random.choice(allowed_chars)
        print(one_id)

print(user_id_gen_by_user())

'''3. Write a function named rgb_color_gen. It will generate rgb colors (3 values
ranging from 0 to 255 each).'''
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
print('RGB',rgb_color_gen())

#Level 2
'''1. Write a function list_of_hexa_colors which returns any number of hexadecimal
colors in an array (six hexadecimal numbers written after #. Hexadecimal
numeral system is made out of 16 symbols, 0-9 and first 6 letters of the
alphabet, a-f. Check the task 6 for output examples).'''
def list_of_hexa_colors(n):
    color = []
    for i in range(n):
        hex_color = '#'
        for j in range(6):
            hex_digit = random.choice('0123456789abcdef')
            hex_color += hex_digit
        color.append(hex_color)
    return color
print(list_of_hexa_colors(5))

'''2. Write a function list_of_rgb_colors which returns any number of RGB colors in
an array.'''
def list_of_rgb_colors(n):
    colors =[]
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255) 
        colors.append((r, g, b))
    return colors
print(list_of_rgb_colors(5))

'''3. Write a function generate_colors which can generate any number of hexa or
rgb colors.'''
def generate_colors(n,color_type):
    color = []
    if color_type == "hexa":
        for i in range(n):
            hex_color = '#'
            for j in range(6):
                hex_digit = random.choice('0123456789abcdef')
                hex_color += hex_digit
            color.append(hex_color)

    else:
        for i in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255) 
            color.append((r, g, b))
    return color
print(generate_colors(5, 'hexa'))
print(generate_colors(5, 'rgb'))

#level 3
'''1. Call your function shuffle_list, it takes a list as a parameter and it returns a
shuffled list'''
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1, 2, 3, 4, 5]))

'''2. Write a function which returns an array of seven random numbers in a range
of 0-9. All the numbers must be unique.'''
import random

def generate_unique_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

print(generate_unique_numbers())
