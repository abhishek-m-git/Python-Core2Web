def outer():
	def inner():
		print("In Inner")
	inner()
	print("In Outer")
	inner()
		
print("Start")
outer()
print("End")
