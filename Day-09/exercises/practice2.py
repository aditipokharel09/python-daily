# 1. Driving Age Check
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    wait_years = 18 - age
    print(f"You need {wait_years} more years to learn to drive.")

# 2. Age Comparison
my_age = 25
your_age = int(input("Enter your age: "))

if my_age == your_age:
    print("We are the same age!")
else:
    diff = abs(my_age - your_age)
    year_text = "year" if diff == 1 else "years"
    
    if your_age > my_age:
        print(f"You are {diff} {year_text} older than me.")
    else:
        print(f"I am {diff} {year_text} older than you.")

# 3. Number Comparison
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")