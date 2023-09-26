s=input("Enter the string:\n")
l1=list(s)
l=[]
for i in l1:
    if i not in l:
        l.append(i)
        x=l1.count(i)
        if x>1:
            l.append(str(x))
n=''
for i in l:
    n=n+i
print(n)