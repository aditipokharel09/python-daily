#1.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14
radius = float(input("Enter radius: "))
area = pi * radius * radius
circumference = 2 * pi * radius

print(f"Area: {area}, Circumference: {circumference}")

"""
2. Line Equation (y = 2x - 2)
From the slope-intercept form (y = mx + c):
Slope (m): 2
Y-intercept: Set x = 0 -> y = -2
X-intercept: Set y = 0 -> 0 = 2x - 2 -> x = 1
"""