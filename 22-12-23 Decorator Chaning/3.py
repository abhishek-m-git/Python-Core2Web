#generator basic

def abhi():
    x = 10
    y = 20

    yield x
    yield y

gen = abhi()

print(next(gen))
print(next(gen))
