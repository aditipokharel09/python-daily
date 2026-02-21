def hello_func(greeting, name='you'):
    return '{}, {}'.format(greeting, name)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'art']
info = {'name': 'sara', 'age': 22}

student_info(*courses, **info)
