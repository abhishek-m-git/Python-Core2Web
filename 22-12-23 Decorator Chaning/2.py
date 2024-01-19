#decorator chaining

def decorFun(func):
    def wrapper():
        print("Start Wrapper 2")
        func()
        print("End Wrapper 2")
    return wrapper

def decorRun(func):
    def wrapper():
        print("Start Wrapper 1")
        func()
        print("End wrapper 1")
    return wrapper

@decorFun
@decorRun
def normalFunc():
    print("In Normal Function")

# normalFunc = decorFun(decorRun(normalFunc))
normalFunc()

