import random as r
import math as m
l=eval(input('Enter lower value:'))
u=eval(input('Enter upper value:'))
x=r.randint(l,u)
print("you have only",round(m.log(u-l+1,2)),"chances to guess the number")
c=0
while c<m.log(u-l+1,2):
    c=c+1
    guess=eval(input("guess the number:"))
    if x==guess:
        print("Congratulations !! you did it in",c,"try")
        break
    elif x>guess:
        print("you guess too small")
    elif x<guess:
        print("you guess to high")
if c>m.log(u-l+1,2):
    print("random guess number is",x)
    print("Better luck next time")