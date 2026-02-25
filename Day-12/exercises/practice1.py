from functools import reduce

countries = ['USA', 'UK', 'Nepal', 'Denmark', 'Russia', 'Iceland']
names = ['prashamsha', 'Aditi', 'Aakriti', 'Aashrab']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3. Define a call function (callback)
def uppercase_it(string):
    return string.upper()

# 4-6. Printing using for loops
for country in countries: print(country)
for name in names: print(name)
for num in numbers: print(num)