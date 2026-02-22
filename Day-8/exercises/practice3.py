it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length
print(f"Length of it_companies: {len(it_companies)}")

# 2. Add 'Twitter'
it_companies.add('Twitter')

# 3. Insert multiple companies
it_companies.update(['Tesla', 'Netflix', 'Reddit'])

# 4. Remove one company
it_companies.remove('Facebook')

# 5. Difference between remove and discard
# .remove() raises a KeyError if the item doesn't exist.
# .discard() does nothing (no error) if the item is missing.