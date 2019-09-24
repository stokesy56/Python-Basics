user_input = input('Would you like to play this game?').lower()
count = 0
while user_input != 'no':
    number_input = int(input('Please enter a number'))
    while count < number_input:
        count += 1
        if count % 3 ==0 and count % 5 == 0:
            print('POCTOC!')
        elif count % 5 == 0:
            print('TOC!')
        elif count % 3 == 0:
            print('POC!')
        else:
            print(count)
    input_2 = input('Do you want to continue playing?').lower()
    print(input_2)
    if input_2 != 'no':
        print('cool')
    else:
        print("OK you have exited the game")
        break
else:
    print('You have exited the game')
