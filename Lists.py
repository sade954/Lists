#Creating literals
my_list = [1,2,3,4,5]
my_list
[1,2,3,4,5]

#Creating a list that has strings, integers, float and boolean
other_list = ['a',1,1.0,False]
other_list
['a',1,1.0,False]

#Indexing operations
my_list[0]
1
my_list[2]
3

#Checking the length
len(my_list)
5

#Get a subsection of a list by slicing
my_list[0:2]
[1,2]
my_list[1:]
[2,3,4,5]
my_list[:3]
[1,2,3]

#Stepping
my_list[0::1]
[1,2,3,4,5]
my_list[0::2]
[1,3,5]

#Assign to a position in a list/modifying the list in place
my_list[0] = 'a'
['a',2,3,4,5]

#Concatenate lists
my_list += [8,9,10]
['a'2,3,4,5,8,9,10]


#Assign a value inside of a list
my_list[1:3] = ['b','c']
my_list
['a','b','c' 4,5,8,9,10]
my_list[3:5] =['d','e''f']
my_list
['a','b','c','d','e''f',,8,9,10]
my_list = ['a','b','c','d',5,6,7]
my_list[4:] = []
my_list
['a','b','c','d']

#Removing items from a list
del my_list[0]
my_list
[b','c','d']
