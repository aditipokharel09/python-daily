# 1. Iterate 0 to 10
print("--- 0 to 10 ---")
for i in range(11):
    print(i)

count = 0
while count <= 10:
    print(count)
    count += 1

# 2. Iterate 10 to 0
print("--- 10 to 0 ---")
for i in range(10, -1, -1):
    print(i)

count = 10
while count >= 0:
    print(count)
    count -= 1

# 3. Hash Triangle (7 calls to print)
print("--- Triangle ---")
for i in range(1, 8):
    print('#' * i)

# 4. Nested Loops for 8x8 Grid
print("--- 8x8 Grid ---")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print() # Moves to next line after each row