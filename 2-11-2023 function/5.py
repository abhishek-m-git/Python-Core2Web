def outer():
	def inner1():
		print("In Inner1")

	def inner2():
		print("In Inner2")
	return inner1,inner2

retObj = outer()
for i in retObj:
	i()

	
