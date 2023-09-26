n=int(input("Enter the value of n:"))
def fibbonacci(n):
    if n<0:
        print("Enter input is wrong so please try again\n")
    elif n==0:
        return 1
    elif n==1 or n==2:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
f=fibbonacci(n)
print(f"fibbonacci of {n} is {f}")