# cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford', 'Corvette']
#
# #syntax
# # for <placeholder> in <iteratable>:    #don't forget the colon
#     #block of code
#     #indented
#
# for car in cars:
#     print(car)
#
# embedded_list = [['filipe', 'Francis'], ['Mustafa', 'David', 'Jillian']]
#
# for data in embedded_list:
#     print(data)
#     for name in data:
#         print(name.capitalize())

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'comlete modules': ['sword', 'augmented senses', 'no face', 'no name']
}
number = 0
for key in student1:
    number += 1
    print(f'{number} - {key}: {student1[key]}')

students = {
    'student1': student1,
    'student2': {
    'name': 'Jimmy Neutron',
    'stream': 'Rocket Science',
    'grade': 2000,
    'comlete modules': ['Super Rockets', 'Advanced AI', 'Handling you super smartness']
    }
}
print('\n')

number1 = 0
for key in students['student2']:
    number1 += 1
    print(f"{number1} - {key}: {students['student2'][key]}")

print('\n')
number2 = 0
for key in students:
    for key1 in students[key]:
        print(f"{key1}, {students[key][key1]}")