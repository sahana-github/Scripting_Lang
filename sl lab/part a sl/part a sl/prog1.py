a=[]
size=int(input("Enter size of list"))
for i in range(0,size):
	ele=int(input("enter elements of list"))
	a.append(ele)
print("The list contains",a)
mini=min(a)
maxi=max(a)
print("Minimum and maximum elements are :", mini, maxi)

ele=int(input("Enter new element to be inserted"))
pos=int(input("Enter position of the element"))
a.insert(pos,ele)

print("The modified list as follows:",a)

ele=int(input("Enter element to be removed"))
a.remove(ele)
print("The modified list as follows:",a)

ele=int(input("Enter element to be found"))
if ele in a:
	print("Element is found at",a.index(ele))
else:
	print("Element not found")
