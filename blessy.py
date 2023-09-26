import random as r
import math 
l=int(input("enter lower value:"))
u=int(input("enter upper value:"))
x=r.randint(l,u)
print(round(math.log(u-l+1,2)))
count=0
while count<math.log(u-l+1,2):
    count+=1
    guess=int(input("Enter the guess number:"))
    if guess==x:
        print("win")
        break
    elif guess>x:
        print("greater")
    elif guess<x:
        print("smaller")
if count>math.log(u-l+1,2):
    print("lost")