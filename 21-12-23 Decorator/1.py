#calling two inner function from outside

def outer():
    print("This is outer function")
    def inner1():
        print("This is inner1 function")
    def inner2():
        print("This is inner2 function")    
    return inner1,inner2

# ret1,ret2 = outer()
# ret1()
# ret2()


#using for loop
ret = outer()
for x in ret:
    x()