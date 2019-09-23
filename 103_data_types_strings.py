# String
# these are a list of characters put together
# defined by '' or ""

my_string = 'Amazing Grilled Fish'
print(type(my_string))
print(my_string)

# Join of strings - concatenation
first_name = 'Boris'
last_name = 'Becker'
full_name = first_name + ' ' + last_name
print(full_name)
print(first_name[0]) #prints first letter of string

# Interpolation
name = 'Rachel'
welcome_message = 'hey there how you doin?'
print(f'hey there {name} how you doin?') #f at beginning of string # can use {} to interpolate variables inside

# Useful Methods for strings
my_string = ' Hello this is an amazing string         '

# .count()
print(my_string.count('i'))
print(my_string.count(' '))

# .len()
print(len(my_string))

# strip()
print(my_string.strip())

# .lower()
print(my_string.lower())

# .upper()
print(my_string.upper())

# .capitilize()
print(my_string.strip().capitalize())

# .replace(arg_int, arg_two)
print(my_string.replace('an', 'THE'))

# .split(arg) -->
print(my_string.split(' '))