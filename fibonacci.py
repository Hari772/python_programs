def fib(n):
    if n<0:
        print("Entre the correct input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the number:"))
fib(n)
print(f"fibonacii of number  \t {n} \t :{fib(n)}")
