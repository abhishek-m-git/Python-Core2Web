class Parent:
	z = 30

	def __init__(self):
		print("In constructor")
		self.x = 10
		self.y = 20

	def dispData(self):
		print(self.x)
		print(self.y)

	@classmethod
	def dispParent(cls):	
		print(cls.z)

	def __del__(self):
		print("In cons")

obj = Parent()
obj.dispData
obj.dispParent() 
