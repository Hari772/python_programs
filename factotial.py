def factorial():
    
    
    n=int(input("Enter the value of n:\n"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of a given {n} is {fact}")
#if __name__=="__main_":
factorial()
