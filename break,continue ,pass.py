n=int(input("Enter the value of n:"))
i=1
print("Using Pass statement")
while i<n:
    if i%2==0:
        pass
    else:
        print(i)
    i=i+1
print("Using break Statement")    
for i in range(1,n+1):
    
    if i%5==0:
        break
    print(i)

print("using continue statement")
for i in range(1,n+1):
    if i%2==0 or i%5==0:
        continue
    print(i)
