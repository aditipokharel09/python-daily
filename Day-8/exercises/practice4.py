A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B (Union)
A_union_B = A.union(B)

# 2. Find A intersection B
A_intersect_B = A.intersection(B)

# 3. Is A subset of B?
is_subset = A.issubset(B) 
print(f"Is A a subset of B? {is_subset}")

# 4. Are A and B disjoint sets? (No shared items)
is_disjoint = A.isdisjoint(B)

# 5. Join A with B and B with A
# Note: Union is commutative, so result is the same
A_with_B = A.union(B)
B_with_A = B.union(A)

# 6. Symmetric difference between A and B
# (Items in either A or B, but NOT both)
sym_diff = A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B