it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 22. Remove the middle IT company or companies
del it_companies[len(it_companies) // 2]

# 23. Remove the last IT company from the list
it_companies.pop()

# 24. Remove all IT companies from the list (Clear the content)
it_companies.clear()

# 25. Destroy the IT companies list (Delete the variable entirely)
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end

# 27. Copy the joined list to full_stack, then insert Python and SQL after Redux
full_stack = joined_list.copy()
# Redux is at index 4, so we want Python at index 5 and SQL at index 6
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

print(full_stack)