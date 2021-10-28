from functools import reduce
mylist=[1,2,3,4,5,6]
print("Original",mylist)
newlist=[x*3 for x in mylist]
print("New",newlist)
or_sum = reduce(lambda x,y: x+y,mylist)
print("Original sum",or_sum)
new_sum = reduce(lambda x,y: x+y,newlist)
print("New sum",new_sum)

