n=int(input("enter the value of the rows:"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=' ')
    print()
