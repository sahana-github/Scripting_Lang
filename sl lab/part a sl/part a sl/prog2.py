class Rectangle:
	def __init__(self):
		self.l = int(input("Enter length"))
		self.b = int(input("Enter breadth"))
	def area(self):
		print("The area of the given rectangle is",self.l*self.b)

R=Rectangle()
R.area()
