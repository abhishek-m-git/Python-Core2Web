def outer(x,y):
	def inner():
		print("In Inner")

	print("In Outer")
	return inner

retObj=outer(10,20)
retObj()
