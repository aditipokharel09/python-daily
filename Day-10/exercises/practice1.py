# Iterating 0 to 10
print("0 to 10 (For):", end=" ")
for i in range(11):
    print(i, end=" ")

print("\n0 to 10 (While):", end=" ")
count = 0
while count <= 10:
    print(count, end=" ")
    count += 1

# Iterating 10 to 0
print("\n\n10 to 0 (For):", end=" ")
for i in range(10, -1, -1):
    print(i, end=" ")

print("\n10 to 0 (While):", end=" ")
count = 10
while count >= 0:
    print(count, end=" ")
    count -= 1