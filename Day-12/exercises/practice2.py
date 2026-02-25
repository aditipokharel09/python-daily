
from functools import reduce

countries = ['USA', 'UK', 'Nepal', 'Denmark', 'Russia', 'Iceland']
names = ['prashamsha', 'Aditi', 'Aakriti', 'Aashrab']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. Map: countries to uppercase
upper_countries = list(map(lambda x: x.upper(), countries))

# 2. Map: numbers to square
squared_numbers = list(map(lambda x: x**2, numbers))

# 3. Map: names to uppercase
upper_names = list(map(lambda x: x.upper(), names))

# 4. Filter: contains 'land'
land_countries = list(filter(lambda x: 'land' in x, countries))

# 5. Filter: exactly six characters
six_char_countries = list(filter(lambda x: len(x) == 6, countries))

# 6. Filter: six letters or more
six_plus_countries = list(filter(lambda x: len(x) >= 6, countries))

# 7. Filter: starts with 'E'
e_countries = list(filter(lambda x: x.startswith('E'), countries))

# 8. Chaining: example (Filter countries with 'land', then uppercase them)
chained = list(map(lambda x: x.upper(), filter(lambda x: 'land' in x, countries)))

# 9. Function to return only string items
def get_string_lists(lst):
    return [item for item in lst if type(item) == str]

# 10. Reduce: sum of numbers
total_sum = reduce(lambda a, b: a + b, numbers)

# 11. Reduce: concatenate countries into a sentence
sentence = reduce(lambda a, b: f"{a}, {b}", countries) + " are north European countries"
# Note: To get the "and" perfectly, you'd usually slice the list first, 
# but this is the pure 'reduce' way!