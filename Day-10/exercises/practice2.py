# Triangle Pattern
for i in range(1, 8):
    print("#" * i)

# 8x8 Grid
print("\n8x8 Grid:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print() # New line after each row

for i in range(11):
    print(f"{i} x {i} = {i * i}")