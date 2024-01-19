#Decorator programm

def decorFun(Func):
    def wrapper():
        print("Start of Wrapper")
        Func()
        print("End of Wrapper")
    return wrapper

@decorFun
def normalFunction():
    print("This is Normal Function")

#normalFunction = decorFun(normalFunction)
normalFunction()
