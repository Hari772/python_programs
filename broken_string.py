n=''
m=''
for i in range(int(input())):
    n=int(input())
    s=input()
    if s[:n//2]==s[n//2:]:
        print("YES")
    else:
        print("NO")
    