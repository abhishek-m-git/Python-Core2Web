#WAP to print the sum numbers upto n

x =int(input("Enter Number : "))
sum = 0 
i =1

while(i<=x):
    sum=sum+i
    i+=1

print(f"Sum of numbers upto {x} is {sum}")