def outer(x,y):
	def inner(a,b):
		print("In Inner")
		return a+b

	print("In outer")
	print(x+y)
	return inner

retObj = outer(10,20)
innerObj = retObj(40,50)
print(retObj)
