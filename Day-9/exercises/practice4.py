person = {
    'first_name': 'Aditi',
    'last_name': 'Pokharel',
    'age': 21,
    'country': 'Nepal',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street', 'zipcode': '02210'}
}

# Skill checks
if 'skills' in person:
    # Middle skill
    middle_index = len(person['skills']) // 2
    print(f"Middle skill: {person['skills'][middle_index]}")
    
    # Python check
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

    # Developer types
    skills = person['skills']
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif set(['Node', 'Python', 'MongoDB']).issubset(set(skills)):
        print("He is a back end developer")
    elif set(['React', 'Node', 'MongoDB']).issubset(set(skills)):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Final check
if person['is_married'] and person['country'] == 'Nepal':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. She is not married.")