name = 'Rory'
last_name = 'Stokes'
age = 22
eye_colour = 'blue'
hair_colour = 'greyish-brown'

name = input('What is your name?').capitalize()
last_name = input('What is your last name?').capitalize()
age = int(input('What is your age?'))
eye_colour = input('What is your eye colour')
hair_colour = input('What is your hair colour?')

print(f'Hello {name}! Welcome, your age is {age}, your eyes are {eye_colour} and your hair is {hair_colour}')

birth_year = 2019 - age
print(f'You said your age was {age}, so you were born in {birth_year}!')
