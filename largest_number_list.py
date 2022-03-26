'''Given an non-empty list find the largest elements in list'''
l1=[10,5,29,8]
l2=[30,30,20]
l3=[4]

# we can use the built-in function max(l)
# but we have to write our custom function to get the largest element in the list
# approach - 1
def getmax(l):
    for i in l:
        for j in l:
            if j>i:
                break
            else:
                return i
print(getmax(l2))
# time complexity for the above function will be: big o of n-square -- example: list sorted in increasing order
# in this we will run the loop one time, two time...n times i.e. n(n+1) times
# optmising the code to make the time complexity linear
# time complexity for the following code will be theta-n as we are comparing each element once only
def getmax(l):
    if not l:
        return None
    else:
        res=l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res=l[i]
        return res  
