# Dictionaries
# All fun and games keep our crazy ex list.. but we also need more info
# Introducing dictionaries!

#Dictionaries are defined using {}
# They are organised with keys that point to values
# Much like looking up something on a dictionary or information about a contact on our phones
# Thus in our phone, the contact Filipe Paiva will hold lot's of info for this entry i.e phone number, email, address etc...

#syntax
# dict_name = {'example_key': 'value', 'example_key': 'value'}

#defining a simple dictionary with

dictionary_crazy_ex = {
'Carolina': 'she was actually nice',
'Arthur': 'bit of a drinker'
}

print(dictionary_crazy_ex)

#Accessing values - use the key!
print(dictionary_crazy_ex['Carolina'])

#Adding a new key, pair value
dictionary_crazy_ex['Kyle'] = 'Likes monster'
print(dictionary_crazy_ex)

dictionary_crazy_ex['Kyle'] = 'REALLY Likes Monster'
print(dictionary_crazy_ex)

#Get out all of the keys
print(dictionary_crazy_ex.keys())

#Get out all of the keys
print(dictionary_crazy_ex.values())

#Remove an entry
dictionary_crazy_ex.pop('Kyle')
print(dictionary_crazy_ex)


## Better example of dictionary

crazy1 = {
    'Name': 'Carolina',
    'Phone': '07842715517',
    'address': 'Location 1, at places',
    'know places to avoid': ['Milan', 'Lisbon', 'Tavira']
}
print(crazy1)