#1.Declare your age as integer variable
age = int(21)
height = float(5.4)

z = 3 + 5j #complex number 

#2.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
import math
base = float(input('enter the base: '))
height = float(input('enter the height: '))
area = 0.5 * base * height
print(area)

#3. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

import math
side_a = float(input('enter the a: '))
side_b= float(input('enter the b: '))
side_c = float(input('enter the c: '))
perimeter = side_a + side_b + side_c
print(perimeter)



#4. Calculate the slope, x-intercept and y-intercept of y = 2x -2

import numpy as np
m = 2
b = -2
y_intercept = (0, b) # y-intercept is when x = 0
x_intercept = (1,0) # x-intercept is when y = 0 -> 0 = 2x - 2 -> 2 = 2x -> x = 1
print(f"Slope (m): {m}")
print(f"y-intercept: {y_intercept}")
print(f"x-intercept: {x_intercept}")


