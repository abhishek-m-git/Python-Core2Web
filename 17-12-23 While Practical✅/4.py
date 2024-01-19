#WAP to calculate factorial of given number 

x = int(input("Enter a number You want to find the Factorial : "))
y = x
fact = 1

while(x>=1):
    fact=fact*x
    x=x-1
print(f"Factorial of {y} is {fact}")