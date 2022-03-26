'''List comprehensions are the ways to write the functions/codes in shorter way'''
# Approach -1 : Find the even and odd items from the list
l=[10,20,30,40,80,10,50,51,79,9,11,60,11,11,80,90,100]
even=[]
odd=[]

for x in l:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)

# Approach -2 : Find the even and odd items from the list using LIST Comprehensions
def getevenodd(l):
    even1=[x for x in l if x%2==0]
    odd1=[x for x in l if x%2 !=0]
    return even, odd

even1,odd1=getevenodd(l)
print(even1)
print(odd1)


# Finding smallest items compared to x (input by user) using list comprehensions
y=int(input("Enter a number here:"))
small_number=[x for x in l if x<y]
print(small_number)

# examples of some other list comprehensions
# getting all the vowels from the string
st="it is a beautiful day"
l1=[x for x in st if x in "aeious"]
print(l1)

# getting string starting with "be"
l2=[x for x in st if x.startswith("be")]
print(l2)

# getting square of all the elements withing range 6 i.e. 0,1,2,3,4,5 
l3=[x*2 for x in range(6)]
print(l3)

# using startswith in list comprehension
l4=['abc','def','ghi','jkl','gno','gqr']
l5=[x.upper() for x in l4 if x.startswith("g")] # this will get output in upper case
print(l5)

# creating sets using list comprehension
# we use {} for creating lists than []
# set contains only distinct items unlike lists
# so, final set will only have unique values and drop any repeated ones
l6={x for x in l if x%2==0} #even 
l7={x for x in l if x%2 !=0} #odd
print(l6)
print(l7)

# creating dict using list comprehensions
# here we are creating key-value pair by taking cube of every element in l
# here the list element will be key and cube will be value in dict d1
d1={x:x**3 for x in l}
print(d1)

d2={x:f"ID{x}" for x in range(5)}
print(d2)

l8=[101,102,103]
l9=["abc","def","ghi"]
d3={l8[i]:l9[i] for i in range(len(l8))}
print(d3)

# better way of creating dict from two lists: zip()
# zip() is a built-in function, it takes multiple iterables like lists, tuple, string, etc
# it creates mapping of these items in the iterables 
# like 101 will be mapped with abc and so on ( from l8 and l9 respectively)
# there mappings will be a tuple, and dict can easily create dict from these tuples
d3=dict(zip(l8,l9))
print(d3)

# inverting the key-value pair in dict uisng list-comprehension
# that is we are making values as keys and keys as values
d4={101: 'abc', 102: 'def', 103: 'ghi'}
d5={v:k for (k,v) in d4.items()}
print(d5)
