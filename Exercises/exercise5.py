name = input('What is your name?').capitalize()
last_name = input('What is your Last name?').capitalize()
age = int(input('How old are you?'))
age_of_mother = int(input('How old is your mother?'))
skill1 = input('Tell me a skill you have')
skill2 = input('Tell me a another skill you have')
skill3 = input('Tell me a another skill you have')

print(f'Hi {name} {last_name}, I hope you are well. You have told me that you are {age} and your mother is {age_of_mother}. You have also said that you have these three skills: {skill1}, {skill2} and {skill3}. WOW you are amazing!')

age_difference = age_of_mother - age
print(f'Wow your mother is {age_difference} years older than you!')
list_skills = [skill1,skill2,skill3]
