n=int(input("Enter the value of n:\n"))
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
factorial=fact(n)
print(f"factorial of {n} is {factorial}\n")

# print('''HI I I AM HARIPRASAD DUVVURU''')