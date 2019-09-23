# As a user I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# need to ask user for input
# need to check if this input matches a magic number


magic_number = 22
magic_input = int(input('Can you guess the magic number?'))
print('Your guess was ',magic_input == magic_number)