ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# 2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# 3. Find the median age
ages.sort() # Re-sorting because we added new items
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]

# 4. Find the average age
average_age = sum(ages) / len(ages)

# 5. Find the range of the ages (max minus min)
age_range = max_age - min_age

# 6. Compare the value of (min - average) and (max - average), use abs()
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
comparison = "Min difference is larger" if diff_min > diff_max else "Max difference is larger"

# --- Level 2: Countries List ---
# (Using a sample list since the original 'countries' list wasn't provided)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# 1. Find the middle country(ies)
mid_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[mid_index - 1 : mid_index + 1]
else:
    middle_countries = [countries[mid_index]]

# 2. Divide the countries list into two equal lists
# If odd, the first half gets the extra one.
split_limit = (len(countries) + 1) // 2
first_half = countries[:split_limit]
second_half = countries[split_limit:]

# 3. Unpack the first three countries and the rest as scandic countries
first, second, third, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print(f"Median: {median_age}, Average: {average_age}")
print(f"First Half: {first_half}")
print(f"Scandic: {scandic_countries}")