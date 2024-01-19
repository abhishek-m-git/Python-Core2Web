#WAP to calculate the sum of first 10 even numbers

sum=0
i=1
while(i<=20):
    if(i%2==0):
        sum=sum+i
    i+=1
print ("Sum of first 10 even numbers is",sum)