n=input()
str1=list(n)
print(str1)
lc=0
uc=0
d=0
for i in str1:
    if i>="A" and i<="Z":
        uc+=1
    elif i>="a" and i<="z":
        lc+=1
    elif i>="0" and i<="9":
        d=d+1
    else:
        pass
c=lc+uc
print("characters=",c)
print("digits=",d)
