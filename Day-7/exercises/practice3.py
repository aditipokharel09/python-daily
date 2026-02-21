
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper() # Changes GOOGLE to uppercase

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# 15. Check if a certain company exists in the it_companies list
does_exist = 'Apple' in it_companies
print(f"Is Apple in the list? {does_exist}")