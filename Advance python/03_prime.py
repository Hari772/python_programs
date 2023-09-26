'''WE CAN  FIND THE  n no of prime numbers .............'''

import sympy as sp

l=[]
n=int(input("Enter the value of n:\n"))

for i in range(1,n+1):
    l.append(i)
print(l)
print(f"PRIME ARE BELOW {n}:.......")
print(f"Total prime numbers between 1 to {n} is:{sp.primepi(n)}")
a=[]
for j in l:
    if sp.isprime(j)==True:
        a.append(j)
print(f"List of prime numbers below {n} is :",a)

            
