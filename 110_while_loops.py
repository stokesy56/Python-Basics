import time
# While loops

# keeps looping and iterating until a condition is met
# or it comes into a BREAK statement

#syntax 1
# while <condition>
    # block

# syntax 2
# while <condition>
    # block
    # if <condition>:
        # break

# counter = 0
# while counter < 5:
#     print(counter)
#     print('bla')
#     counter += 1
#     time.sleep(1)
#
# while True:
#     print('Waaaaaaaaaah')
#     if counter > 10:
#         break
#     counter += 1
#
# while True:
#     print('what up jigglpuff?')
#     user_input = input().lower()
#     if user_input == 'exit':
#         break
#     elif user_input == 'cute':
#         print('Ahhh Jigglypuff ... <3')
#     else:
#         print('JJJJJJJIIIIIIIIIIGGGGGGGGGGGLLLLLLLLYYYYYYYYYPPPPPPPPPPPUUUUUUFFFFFFFFFF!!!!!!!!!!')

user_input = input('Hey do you want to be here?').lower()
while user_input != 'no':
    print("I'm so glad you're here please don't leave me")
    input_2 = input('Do you still want to be here?')
    print(input_2)
    if input_2 != 'no':
        print('cool')
    else:
        print("OK you have offended me severely")
        break
else:
    print("OK you have offended me severely")

counter = 0
max_length = len('cars')

cars = ['volvo', 'skoda', 'ferarri', 'lambo']

while counter < max_length:
    print(counter + 1, '--', cars[counter].capitalize())
    counter += 1