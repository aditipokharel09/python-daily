# 6. Declare it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(f"First: {it_companies[0]}, Middle: {it_companies[len(it_companies)//2]}, Last: {it_companies[-1]}")

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Nvidia')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Tesla')