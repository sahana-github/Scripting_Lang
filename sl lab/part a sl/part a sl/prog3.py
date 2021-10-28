def AtomicDictionary(): 
	Atomic_elements = {"C":"Carbon","B":"Boron","N":"Nitrogen","S":"Sulphur"}
	print(Atomic_elements)
	new_symbol=input("enter the symbol ")
	new_element=input("enter the element ")
	if new_symbol in Atomic_elements.keys():
		print("Key exists and hence value is replaced")
	else:
		print("New key and value added to dictionary")
	Atomic_elements[new_symbol]=new_element
	print(Atomic_elements)
	print("length of dictionary -",len(Atomic_elements))
	search_key=input("enter the symbol to search ")
	if search_key in Atomic_elements.keys():
		print(Atomic_elements[search_key])
	else:
		print("Key does not exist in dictionary")



'''Place this in a different python script and call the fucntion'''

AtomicDictionary()

