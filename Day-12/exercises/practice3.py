from functools import reduce

countries = ['USA', 'UK', 'Nepal', 'Denmark', 'Russia', 'Iceland']
names = ['prashamsha', 'Aditi', 'Aakriti', 'Aashrab']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 12. Categorize countries
def categorize_countries(pattern):
    # This assumes you have the full list of countries loaded
    return [c for c in countries if pattern in c]

# 13. Dictionary of starting letters
def count_starting_letters(lst):
    counts = {}
    for country in lst:
        letter = country[0]
        counts[letter] = counts.get(letter, 0) + 1
    return counts

# 14 & 15. First/Last 10 (Using slicing)
def get_first_ten(lst): return lst[:10]
def get_last_ten(lst): return lst[-10:]