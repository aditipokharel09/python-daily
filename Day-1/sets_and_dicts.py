cs_courses = {'math', 'sci', 'comp', 'social', 'english'}
art_courses = {'sci', 'math', 'art', 'design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

student = {'name': 'aditi', 'age': 20, 'courses': ['math', 'compsci']}
student.update({'name': 'anshu', 'age': 16, 'phone': '555-555'})
print(student)

del student['age']
print(student)
