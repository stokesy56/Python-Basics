# Lists
# list keep object in order of index
# it's defined by []

#example list
crazy_exes = ['Carolina', 'JSON', 'Arthur', 'Lana!']

#print and show type (Read All)
print(crazy_exes)
print(type(crazy_exes))

#Get a particular record out (Read one)
#Lists are organised with index
print(crazy_exes[0])
print(crazy_exes[-1]) #minus sign reads from end of index inwards

#Change a reccrd in specific index?
crazy_exes[3] = 'LANA!!! beware danger zone'
print(crazy_exes[3])

#Add something to list - append()
crazy_exes.append('Syril Figus')
print(crazy_exes)

#Insert in specific location
crazy_exes.insert(3,'Malorie')
print(crazy_exes)

#Remove something from lift
crazy_exes.remove('JSON')
print(crazy_exes)

#Remove using index
crazy_exes.pop(1)
crazy_exes.pop() #removes last entry
print(crazy_exes)

#Mixed data and list
#Lists can have many data types
hybrid_list = ['this is a string', 12, 66, 'hello', [1,2,3], [1,2,2]]

#Tuples --> Imutable lists
# They do not change
#syntax:
# my_tuple = ()
my_tuple = (2, 'hello', 22, 'more values')
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

#range slicing
print(crazy_exes[:1]) # 0 to 1, not inclusive
print(crazy_exes[1:3])

# Jumping/slicing
example_list = [0,1,2,3,4,5]
print(example_list[::2])
print(example_list[1::2])