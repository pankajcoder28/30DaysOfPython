#ques1
print("my age =",18)
#ques2
print("my height = ",5.8)
#q3
com = 1+4j
#q4
base = int(input("enter the base ="))
height = int(input("enter height ="))
area = 0.5 * (base * height)
print("the area of a triangle is  ", area)
#q5
a = int(input("enter side a ="))
b = int(input("enter side b ="))
c = int(input("enter side c ="))
peri = a+b+c
print("the  perimeter of triangle is ",peri)
#q6
leng = int(input("enter the length = "))
wid = int(input("enter the width = "))
print("area is : ",leng*wid)
print("perimeter is : ", 2*(leng + wid))
#q7
r = int(input("enter radius = "))
print("area = ",3.14 * r **2)
print("circumference = ",2*3.14*r)
#q8
# Equation: y = 2x - 2
slope1 = 2
x_for_y_intercept = 0
y_intercept = 2 * x_for_y_intercept - 2

x_intercept = (0 + 2) / 2

print("Slope (m):", slope1)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

#q9
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance betweenpoint (2, 2) and point (6,10)

x1,y1=2,2
x2,y2=6,10

slope2 = int((y2-y1)/(x2-x1))
dist = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("slope = ",slope2)
print("distance = ",dist)
#q10

print(slope1 == slope2)
#q11
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values andfigure out at what x value y is going to be 0.
x =-3
y = ((-3**2) + 6*(-3) + 9)
print(y)
#12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') is not len('dragon'))
#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')
#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon.")
#15.There is no 'on' in both dragon and python
print(not('on' in 'python' and 'on' in 'dragon'))
#16.Find the length of the text python and convert the value to float and convert it to string
value = len('python')
print(value)
print(float(value))
print(str(value))

#17.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('enter a num :'))
even_check = num %2 ==0
print("Even number - ", even_check)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

float_value = 2.7
f_div = 7//3
print( f_div == int(float_value))
#19. Check if type of '10' is equal to type of 10

print(type('10') == type(10))

#20. Check if int('9.8') is equal to 10
print(float('9.8') == 10)

#21.Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hour = int(input('enter hour = '))
r_hour = int(input("enter rate per hour ="))
print("your weekly earning is =  ",hour*r_hour)

#22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

year = int(input("enter number of years "))
print(" you have lived for ",year*365*24*60*60 ,"seconds")
 
#23.Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#2 1 2 4 8
#4 1 4 16 64
#5 1 5 25 125 

print(1 , 1 ,1 ,1, 1)
print(2 ,1, 2, 4, 8)
print(2, 1, 2, 4, 8)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
