# 1. Filter only negative and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# My logic: "Keep 'i' for every 'i' in numbers IF 'i' is less than or equal to 0"
filtered = [i for i in numbers if i <= 0]

# 2. Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# My logic: This is a double loop. "For every sublist in the main list, take every number in that sublist"
flattened = [num for sublist in list_of_lists for num in sublist]

# 3. Create a list of tuples (The Powers Table)
# My logic: The exercise shows (n, 1, n, n^2, n^3, n^4, n^5) for numbers 0-10
powers = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# 4. Flatten and Format Countries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# My logic: I need to reach into the sublist, then the tuple, then uppercase everything and grab the 3-letter code
formatted_countries = [[c[0].upper(), c[0][:3].upper(), c[1].upper()] for sub in countries for c in sub]

# 5. List of Dictionaries
# My logic: Same nesting as above, but wrapping the data in {key: value} pairs
country_dicts = [{'country': c[0].upper(), 'city': c[1].upper()} for sub in countries for c in sub]

# 6. Concatenate names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# My logic: Reach in and use an f-string to join the first and last name
full_names = [f"{n[0]} {n[1]}" for sub in names for n in sub]

# 7. Lambda for Slope (m)
# My logic: Slope formula is (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)