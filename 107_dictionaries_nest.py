# Nested lists and dictionaries

nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice']]

print(nested_list[2][4]) #not best way - can get complicated
variable_nested = nested_list[2]
print(variable_nested[4])

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'comlete modules': ['sword', 'augmented senses', 'no face', 'no name']
}

students = {
    'student1': student1,
    'student2': {
    'name': 'Jimmy Neutron',
    'stream': 'Rocket Science',
    'grade': 2000,
    'comlete modules': ['Super Rockets', 'Advanced AI', 'Handling you super smartness']
    }
}
print(students['student1'])
print(students['student1'].keys())