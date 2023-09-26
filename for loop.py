# displaying 1 to 10 numbers usinf for loop
i=0
n=int(input("Enter the value of n:"))
for i in range(n+1):
    print(f"i value is {i}")

for i in range(0,n+1,2):
    print("even numbers between 0 to 10 is",i)

for i in range(0,n+1,3):
    print("odd numbers between 0 to 10 is",i)
    
