import sympy as sp
n=int(input("Entre thr value of n:\n "))
if sp.isprime(n)==True:
    print(f"{n} is prime number")
else:
    print("It is not prime number")