'''There are various function that can be implemented on LISTS'''

# list with all int dtype
list1=[10,20,30,50,70,10,10]

#list with all string dtype
list2=['efg','abc','gfg','def','abc','gfg']

#list with mix dtype
list3=[10,20,'abc',50,90]

# adding new item/element in list using append() 
list1.append(80)
print(list1)

# inserting item/element at given index
# here insert() takes two parameters--one as the value to insert and other as the index position at which value should be inserted
list3.insert(10,2) 
print(list3)

# checking if an item/element exist in a given list or not
# this will give boolean output i.e. True or False
print(30 in list1)
print('abc' in list2)

# counting the number of time an item/element occured in lst
# using count()
print(list1.count(10))
print(list2.count('abc'))

# checking index of an item/element in a given list
# but before checking the index make sure item exist in the list
# to check if the item ecist in a list -- use "in" statement-- ex: print(10 in list1)
print(list2.index('abc'))
print(list1.index(30))
print(list1.index(30,1,7)) # here we define the range of index where we need to find the item i.e. start and end index

# removing items from the list
print(list1.remove(10)) # only use remove() when we know item exist in the list else it will give ValueError
print(list1.pop()) # removes the last item from the list
print(list2.pop(2)) # removing the item at index 2
del list1[3] # deleting item at index 3
del list3[0:2] # deleting items at index 0 and 1--here index 2 is not included

# getting the maximu value from the list
print(max(list1))
print(max(list2)) # this gives lexographically max value

# getting minimum value from the list
print(min(list1))
print(min(list2)) # this gives lexographically min value

# getting sum of all the value in the list
# note: used on the numerical dtype only
print(sum(list1))

# reversing the list
print(list1.reverse())

# sorting the values in list
# by default it is ascending
print(list2.sort())




