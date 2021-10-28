def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def main():
	try:
		list = eval(input("Enter a list of numbers: "))
		print ("The largest number is: ", Max(list))
	except SyntaxError:
		print ("Please enter comma separated numbers")
	except:
		print ("Enter only numbers")

main()

