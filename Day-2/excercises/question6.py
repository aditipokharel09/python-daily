#1. Check the data type of all your variables using type() built-in function

name = 'aditi pokharel'
age = 21
country = 'nepal'
city = 'kathmandu'
is_married = False
print(type(name))
print(type(age))
print(type(country))
print(type(city))
print(type(is_married))


#2. Using the len() built-in function, find the length of your first name

name = 'aditi pokharel'
print(len(name))

#3. Compare the length of your first name and your last name

first_name = 'aditi'
last_name = 'pokharel'
if (len(first_name)) == (len(last_name)):
    print('OH THEY ARE EQUAL!!')
else:
    print('OH NO THEY ARE NOT EQUAL!!')

"""4. Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
"""

num_1 = 5
num_2 = 4
total = (num_1 + num_2)
total = (num_1 - num_2)
total = (num_1 * num_2)
total = (num_1 / num_2)
total = (num_1 // num_2)
total = (num_1 ** num_2)
print(total)


"""5. The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area."""

import math
radius = float(input("Radius please: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(area)
print(circumference)