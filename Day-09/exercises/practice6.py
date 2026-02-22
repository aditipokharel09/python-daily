# 5. Multiplication Pattern
print("--- Pattern ---")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through a list
tech_stack = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("--- Tech Stack ---")
for item in tech_stack:
    print(item)

# 7. Even numbers 0 to 100
print("--- Evens ---")
for i in range(0, 101, 2):
    print(i)

# 8. Odd numbers 0 to 100
print("--- Odds ---")
for i in range(1, 101, 2):
    print(i)

    # 1. Sum of all numbers 0 to 100
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.")