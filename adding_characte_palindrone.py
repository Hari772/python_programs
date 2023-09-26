str1=input()
n=len(str1)
s=" "
for i in range(0,n):
    temp=str1[i:n]
    if temp==temp[::-1]:
        break
for i in range(i-1,-1,-1):
    s=s+str1[i]
print(s)
