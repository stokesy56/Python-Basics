#Control Flow - If statements
# controls where the code is going to go
# depending on the results of the evaluations that return true or false it runs a block of code or not

#syntax
# if <condition>:
    #block
# elif <condition>:
    #block
# else:
    #block

weather = 'rainy'

if weather == 'rainy':
    print('Wear a coat')
elif weather == 'snowy':
    print('Wear boots and scarf')

age = 17
driver_license = False

if age >= 18 and driver_license == True:
    print("You can vote and drive, wow you're an adult")
elif age >= 18 and driver_license == False:
    print("You can vote and take lessons to drive")
elif age >= 17 and driver_license == True:
    print('Wow you can drive a car!')
elif age >= 17:
    print('You are old enough to take driving lessons')
elif age == 16:
    print('You can drink but you need an older friend to buy you a drink')
else:
    print("You're too young go back to school!")

