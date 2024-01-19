#WAP to Print the first 10 negative numbers which is less than the given number.
#input = -5

x = int(input("Enter The number : "))
i = 1

print("First 10 negative numbers less than -5 are ")

while(i<=10):
    x-=1
    print(x,end =' ')
    i+=1

# print('hello world', end=',')