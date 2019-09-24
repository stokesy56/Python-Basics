user_input = input('Say something to your teacher').lower()
while user_input != "i'm a doctor":
    if user_input.__contains__('?'):
        print('HAHAHA! AHAHAHAHHA!! OMG! What a silly question! Go back to school!')
    elif user_input.__contains__('!'):
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')
    else:
        print('Go back to school!')
    user_input = input('Say something else to your teacher')
else:
    print('Well done! You can now talk to me')