it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 16. Sort the list using sort() method (Alphabetical order)
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]

# 20. Slice out the middle IT company or companies
# For a list of 7, the middle is index 3.
mid = len(it_companies) // 2
middle_companies = it_companies[mid:mid+1] 

# 21. Remove the first IT company from the list
it_companies.pop(0)