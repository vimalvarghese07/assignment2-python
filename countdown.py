n=int(input("Enter the number:"))
countDown=n
while(n>0):
    print(countDown)
    countDown-=1
    if(countDown<=0):
        break