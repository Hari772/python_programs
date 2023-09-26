n=int(input("Enter the number:"))#12345
sum=0
count=0
while n>0:
    rem=n%10
    for i in (1,rem+1):
        if rem%i ==0:
            count=count+1
    if count==2:
         pass
    else:
        sum=sum+rem
    n=n//10
print(sum)