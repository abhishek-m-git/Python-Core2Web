#WAP to print cube of odd numbers up to n in reverse order
#input:15

x = int(input("Enter The number : "))

while(x>=1):
    if(x%2==1):
        print(x*x*x,end=' ')
    x-=1
