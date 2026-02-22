import modules as mn

courses = ['history', 'math', 'physics', 'comp']
index = mn.find_index(courses, 'math')
print(index)

#2nd way for importing modules
from modules import find_index, test
courses = ['history', 'math', 'physics', 'comp']
index = find_index(courses, 'math')
print(index)
print(test)