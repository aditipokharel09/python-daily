courses = ['math', 'sci', 'comp', 'social', 'english']
print(courses[-1])
print(courses[2:])

courses.append('art')
courses.insert(0, 'art')

courses_2 = ['physics', 'chemistry']
courses.extend(courses_2)

courses.remove('math')
courses.pop()
courses.reverse()
courses.sort()
print(courses)

# tuples (immutable)
tuple_1 = ('math', 'sci', 'comp', 'social', 'english')
print(tuple_1)
