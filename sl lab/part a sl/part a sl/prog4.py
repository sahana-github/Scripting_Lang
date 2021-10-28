class Student:
	name = ""
	age = 0
	sublist = []
	def __init__(self,x,y,l):
		self.name = x
		self.age = y
		self.sublist=l
	def accept(self):
		self.name = input("Enter name: ")
		self.age = input("Enter age: ")
		print("Enter marks of subjects\n")
		l = input()
		l = l.split(" ")
		x = []
		for i in range(len(l)):
			x.append(int(l[i]))
			self.sublist = x
	def disp(self):
		print(self.name)
		print(self.age)
		print(self.sublist)





s1 = Student('shri',20,[90,80,95])
s1.disp()

s2 = Student('sanju',23,[60,82,75])
s2.disp()
s2.accept()
s2.disp()

