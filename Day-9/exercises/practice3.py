# 1. Grading System
score = int(input("Enter student score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")

# 2. Season Checker
month = input("Enter month: ").capitalize()
if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")

# 3. Fruit List Check
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print(f"Modified list: {fruits}")