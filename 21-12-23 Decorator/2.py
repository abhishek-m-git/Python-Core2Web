def run():
    print("In run")

def fun(x):
    print("In fun")
    x()

fun(run)