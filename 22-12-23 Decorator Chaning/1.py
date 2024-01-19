#passing argument to decorator(Decor Function)

def decorFunc(func):
    def wrapper(*args):
        print("Start Wrapper")
        val = func(*args)
        print("End Wrapper")
        return val
    return wrapper

@decorFunc
def normalFunc(x,y):
    print("In Normal Function")
    return x+y

# normalFunc = decorFunc(normalFunc)
# print(normalFunc(10,20))


# ret = normalFunc(10,20)
print(normalFunc(10,20))