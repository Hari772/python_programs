def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
num=int(input("Enter the value of num"))
result=factorial(num)
print("factorial of",num,"is",result)
