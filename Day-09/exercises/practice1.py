# 1 & 2: Create dog dictionary and add attributes
dog = {}
dog['name'] = 'Rex'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# 3: Create student dictionary
student = {
    'first_name': 'Aditi',
    'last_name': 'Pokharel',
    'gender': 'Female',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Cybersecurity'],
    'country': 'USA',
    'city': 'Los Angeles',
    'address': '123 Tech Lane'
}

# 4: Get length
student_len = len(student)

# 5: Get skills and check type
skills = student['skills']
print(f"Skills type: {type(skills)}")

# 6: Modify skills
student['skills'].extend(['Git', 'Docker'])

# 7 & 8: Get keys and values as lists
keys_list = list(student.keys())
values_list = list(student.values())

# 9: Change to list of tuples
student_tuples = list(student.items())

# 10 & 11: Deletions
del student['marital_status']
del dog