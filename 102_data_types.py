# Numerical Data types
# - Int, long, float, complex
#  These are numerical data types which we can use numerical operators

# Complex and long we don't use much
# COmplex can have imaginary numbers
# long - are integers of unlimited size

my_int = 10
print(my_int)
print(type(my_int))

# Operator - add, subtract, divide and multiply
# exponential

print(4 / 2)
print(5 // 2)  # keeps it a s integer/ drops decimal
print(3 * 2)
print(3 ** 2)

# Modulus % gives remainder from division of two variables
print(10 % 3)  ##gives 1 there are three 3's in 10 and 1 leftover

# Comparison operator --> outputs boolean value
# == is comparison operator
# < / > is greater/smaller than
# <= is less than or equal to
# >= is greater than or equal to
# != not equal
# is or is not

my_variable1 = 10
my_variable2 = 13

print(my_variable1 == my_variable2)
print(my_variable2 > my_variable1)
print(my_variable2 is 12)
print(my_variable1 is not 11)

#Boolean values
# defined by whether true or false
print(type(True))
print(0 == False)
print(1 == True)

# None
print(None)
print(type(None))
print(bool(None))
print(False == None)
print(False == bool(None))

# Logical AND & OR
a =True
b = False

#using *and* both sides have to be true to result in true
print( a and True)
print((1 == 1) and True)
print((1 == 1)and False)
print(True or False) #prints true - or only requires one thing to be true to return true
