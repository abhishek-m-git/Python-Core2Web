#WAP to print squares of even numbers upto n
#input: 10

i = 1
x = int(input("Enter a Number : "))

while(i<=x):
    if (i%2==0):
        print(i*i,end=' ')
    i+=1
