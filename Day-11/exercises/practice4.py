# 1. Filter negative and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in numbers if i <= 0]

# 2. Flatten list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in list_of_lists for num in sublist]

# 3. List of tuples (Powers)
# Logic: (n, 1, n, n**2, n**3, n**4, n**5)
powers = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# 4. Flatten and Format Countries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[c[0].upper(), c[0][:3].upper(), c[1].upper()] for sub in countries for c in sub]

# 5. List of Dictionaries
country_dicts = [{'country': c[0].upper(), 'city': c[1].upper()} for sub in countries for c in sub]

# 6. Concatenate names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{n[0]} {n[1]}" for sub in names for n in sub]

# 7. Lambda for Slope (m) and Intercept (b)
# Using points (x1, y1) and (x2, y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, m: y1 - (m * x1)