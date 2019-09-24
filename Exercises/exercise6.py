name_dict = {}

name_dict['hero'] = input('Please enter a hero for your story').capitalize()
name_dict['villain'] = input('Please enter a villain for your story').capitalize()
name_dict['activity'] = input('Please enter a random and unusual activity that our hero likes to partake in').lower()
name_dict['beginning'] = input("Please describe a problem your villain is causing starting with the phrase 'he/she is'")
name_dict['middle'] = input("Please enter your hero's solution to this problem starting with the phrase 'to solve this problem he/she'")
name_dict['end'] = input('Please describe a weird and wacky location')

print(f"\n One day {name_dict['hero']} is strolling down the street when suddenly his super instincts tell him that {name_dict['villain']} is causing trouble! \n It seems that {name_dict['beginning']} But not to fear! For {name_dict['hero']} is here! {name_dict['hero']} wants this over with quickly and {name_dict['middle']}. \n Hoorah for {name_dict['hero']}! What a brilliant thing to think of! {name_dict['hero']} celebrates this victory with a trip to {name_dict['end']} where our hero partakes in some {name_dict['activity']}. WOW what an eventful day for our hero {name_dict['hero']}")


