# variables in python
    #variable is a box. You can give it a name and put stuff inside

#giving box name and putting stuff inside
box_variable = 'Books'

#looking inside the box
print(box_variable)

# variabels are mutable - can be changed/reassigned

#Reassigning variable
box_variable = 'CDs'
print(box_variable)

#Reassigning with integer
#variable can have any data type inside
box_variable = 14
print(box_variable)

# important python functions
# print(arg)
print('hello') #printing string
print(box_variable) # printing variable
print('hello', box_variable) #overloading with two arguments

# type(arg)
# output the data type of an object
print(type('hello'))
print(type(14))
print(type(14.0))

#input()
# prompts user for a response
print('whats your name?')
user_response = input()
print(user_response)