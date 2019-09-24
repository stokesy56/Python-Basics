book = {
    'story1': {
        'beginning': 'One day Sharik and miles were at Mcdonalds.',
        'middle': 'The self service machine they are using starts beeping and explodes!',
        'end': 'They are both obliterated by the blast. The end.'
    },
    'story2': {
        'beginning': 'Lennox and Abror were about to watch the Man U game.',
        'middle': 'However when they turned the TV on it exploded!',
        'end': 'They are both obliterated by the blast. The end.'
    },
    'story3': {
        'beginning': 'Vishnu and Jillian were arguing about why Moustapha is always on the phone while waiting for their food to heat up in the microwaves.',
        'middle': 'All of a sudden the microwaves start rattling and violently explode!',
        'end': 'They are both obliterated by the blast. The end.'
    }
}


read_book_input = input('Would you like to read this book?').lower()
while read_book_input != 'no':
    user_input = input('Which story would wou like to read? Story 1, 2 or 3?\n')
    if user_input.__contains__('1'):
        print(f"{book['story1']['beginning']} \n{book['story1']['middle']} \n{book['story1']['end']}\n")
    elif user_input.__contains__('2'):
        print(f"{book['story2']['beginning']} \n{book['story2']['middle']} \n{book['story2']['end']}\n")
    elif user_input.__contains__('3'):
        print(f"{book['story3']['beginning']} \n{book['story3']['middle']} \n{book['story3']['end']}\n")
    else:
        print('You have entered an invalid story, please enter 1, 2 or 3')
    continue_input = input('Would you like to continue reading this book?')
    if continue_input != 'no':
        print('Great!')
    else:
        print('Fair enough, but you should read more.')
        break
else:
    print('Fair enough, but you should read more.')
