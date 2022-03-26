'''
1. Lists are collection of items -- using Arrays at the backend
2. Speciallity of lists are:
    a) allows random access
    b) have dynamic size
    c) allow different types of dtypes as items
'''
# example of list
#empty list
li=[]

# list with all int dtype
list1=[10,20,30,50,70]

#list with all string dtype
list2=['efg','abc','gfg','def']

#list with mix dtype
list3=[10,20,'abc',50,90]

'''
1. Indexing in list -- starts from 0 till n-1, where n=total lenght or number if items in list
2. We can have index from Right-->Left (index starts from 0)
3. we can also have index from Left-->Right (index starts from -1)
'''
# slicing & dicing of lists
# printing entire list
print(list1)
print(list2)
print(list3)

# print item/element at index 3
print(list1[3])
print(list3[2])

# print item/element at index -3
print(list1[-3])
print(list2[-2])