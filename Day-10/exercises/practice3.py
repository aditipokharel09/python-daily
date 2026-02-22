# List iteration
tech_stack = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech_stack:
    print(item)

# Even numbers
print("Evens:", [i for i in range(101) if i % 2 == 0])

# Odd numbers
print("Odds:", [i for i in range(101) if i % 2 != 0])