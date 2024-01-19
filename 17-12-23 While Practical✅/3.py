#WAP to find 7th odd number (start from 1)

count = 0

i = 1

while(i<=100):
    if(i%2==1):
        count+=1
        if(count==7):
            print(i)
            break
    i+=1

    