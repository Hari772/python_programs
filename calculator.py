# *********************** Simple Calculator *******************************
import math as h
print("************************** Simple Calculator ***************************")
print("               1.SUM")
print("               2.DIFFERENCE")
print("               3.MULTIPLICATION")
print("               4.DIVISION")
print("               5.REMAINDER")
print("               6.FLOOR DIVISION")
print("               7.SQUARE")
print("               8.CUBE")
print("               9.SQURE ROOT")
print("               10.FACTORIAL")
print("               11.LOG")
print("               12.GCD")
print("               13.LCM")
print("               14.CUBE ROOT")
print("               15.sine(),cos(),tan(),cot(),sec(),cosec()")
operation=eval(input())
if operation==1:
    a=eval(input("Enter number:"))
    b=eval(input("Enter number:"))
    add=a+b
    print("Sum is...",add)
elif operation==2:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    sub=a-b
    print("Difference is...",sub)
elif operation==3:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    mul=a*b
    print("Multiplication is...",mul)
elif operation==4:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    div=a/b
    print("Division is...",div)
elif operation==5:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    rem=a%b
    print("Remainder is ...",rem)
elif operation==6:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    floor=a//b
    print("Floor Division is ...",floor)
elif operation==7:
    a=eval(input("Enter a:"))
    #b=eval(input("Enter b:"))
    sq=a*a
    print(f"square of {a} is ...{sq}")
elif operation==8:
    a=eval(input("Enter a:"))
    #b=eval(input("Enter b:"))
    cube=a*a*a
    print(f"Cube of {a} is ...{cube}")
elif operation==9:
    a=eval(input("Enter a:"))
    #b=eval(input("Enter b:"))
    sq_root=h.sqrt(a)
    print(f"Square root of {a} is ...{sq_root}")
elif operation==10:
    a=eval(input("Enter a:"))
    #b=eval(input("Enter b:"))
    fact=h.factorial(a)
    print(f"Factorial of {a} is ...{fact}")
elif operation==11:
    a=eval(input("Enter a:"))
    #b=eval(input("Enter b:"))
    log=h.log()
    print(f"log of {a} is...{log}")
elif operation==12:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    gcd=h.gcd(a,b)
    print(f"GCD of {a} and {b} is...{gcd}")
elif operation==13:
    a=eval(input("Enter a:"))
    b=eval(input("Enter b:"))
    
    lcm=h.lcm(a,b)
    print(f"LCM  is...",lcm)
elif operation==14:
    a=eval(input("Enter a:"))
    cube=a**(1/3)
    #cube=int(c)
    print(f"cube root of {a} is...{cube}")

elif operation==15:
    print("********************* TRIGNOMETRIC FUNCTIONS OVER *************************")
    print("               1.sin()")
    print("               2.cos()")
    print("               3.tan()")
    print("               4.cot()")
    print("               5.sec()")
    print("               6.cosec()")
    num=eval(input())
    
    #b=eval(input("Enter b:"))
    if num==1:
        a=eval(input("Enter degree:"))
        b=h.sin(h.radians(a))
        print(f"Returns the sine value of {a} is {b}")
    elif num==2:
        a=eval(input("Enter degree:"))
        b=h.cos(h.radians(a))
        print(f"Returns the cos value of {a} is {b}")
    elif num==3:
        a=eval(input("Enter degree:"))
        b=h.tan(h.radians(a))
        print(f"Returns the tan value of {a} is {b}")
    elif num==4:
        a=eval(input("Enter degree:"))
        b=h.atan(h.radians(a))
        print(f"Returns the cos value of {a} is {b}")
    elif num==5:
        a=eval(input("Enter degree:"))
        b=h.acos(h.radians(a))
        print(f"Returns the cos value of {a} is {b}")
    elif num==6:
        a=eval(input("Enter degree:"))
        b=h.asin(h.radians(a))
        print(f"Returns the cos value of {a} is {b}")
    else:
        print("********************* TRIGNOMETRIC FUNCTIONS OVER *************************")
        print("TRY AGAIN")

else:
    print("********************* Simple Calculator *************************")
    print("**********************TRY ONCE AGAIN LATER **********************")    
    
       


    
    
    
    
    

