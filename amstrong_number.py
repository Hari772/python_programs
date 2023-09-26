'''Let's try to understand Armstrong number.

153 = (1*1*1)+(5*5*5)+(3*3*3)   digits=3
where:  
(1*1*1)=1  
(5*5*5)=125  
(3*3*3)=27  
So:  
1+125+27=153  '''
'''n=int(input("Enter the number:"))
temp=n
sum=0
while temp!=0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if n==sum:
    print("it is a amstrong number")
else:
    print("not amstrong number")'''
n=int(input("Enter the number:"))
temp=n
count=0
sum=0
y=len(str(n))
while temp!=0:
    digit=temp%10
    sum=sum+digit**y
    temp=temp//10
if n==sum:print("Amstrong")
else:print("not Amstrong")