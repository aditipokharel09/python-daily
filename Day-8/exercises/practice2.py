# 1. Unpack siblings and parents
family_members = ("Anna", "Bella", "Chris", "David", "Father", "Mother")
*sibling_names, father, mother = family_members
print("Unpacked siblings:", sibling_names)
print("Father:", father)
print("Mother:", mother)

# 2. Create food tuples
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "spinach", "broccoli")
animal_products = ("milk", "eggs", "cheese")

food_stuff_tp = fruits + vegetables + animal_products
print("Food tuple:", food_stuff_tp)

# 3. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)

# 4. Slice middle item(s)
middle_index = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1: middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]

print("Middle item(s):", middle_items)

# 5. First 3 and last 3 items
print("First 3 items:", food_stuff_lt[:3])
print("Last 3 items:", food_stuff_lt[-3:])

# 6. Delete tuple
del food_stuff_tp
# print(food_stuff_tp)  # ← would raise error if uncommented

# 7. Check Nordic countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Is Estonia Nordic?", "Estonia" in nordic_countries)
print("Is Iceland Nordic?", "Iceland" in nordic_countries)