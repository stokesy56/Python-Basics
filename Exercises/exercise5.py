name = input('What is your name?').capitalize()
last_name = input('What is your Last name?').capitalize()
age = int(input('How old are you?'))
age_of_mother = int(input('How old is your mother?'))
skill1 = input('Tell me a skill you have').lower()
skill2 = input('Tell me a another skill you have').lower()
skill3 = input('Tell me a another skill you have').lower()

print(f'Hi {name} {last_name}, I hope you are well. You have told me that you are {age} and your mother is {age_of_mother}. You have also said that you have these three skills: {skill1}, {skill2} and {skill3}. WOW you are amazing!')

age_difference = age_of_mother - age
print(f'Wow your mother is {age_difference} years older than you!')
list_skills = [skill1,skill2,skill3]

print(f'You have said that your skills are {list_skills[skill1]}, {list_skills[skill2]} and {list_skills[skill3]}')

#Formatted meaning
    # to arrange and organise a string
# to format a string one can use the various methods such as .lower() or .upper() to change the case of a string
    # More example methods of formatting are .capitalize, .split, .strip and many more...
# there is also the .format() method that  allows you to do variable substitutions and value formatting.
    # This lets you concatenate elements together within a string through positional formatting.
