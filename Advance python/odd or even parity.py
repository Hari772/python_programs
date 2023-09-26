num=int(input("Enter the value of some number:\n"))
print(type(num))
strnum=str(num)
print(type(strnum))
print(f"given number is converted to string:{strnum}")
print("counting the numbers of 1's for parity\n")
print("Now checking parity")
x=strnum.count("1")
print(f"no of 1's is {x}")
if x%2==0:
    print(f"{strnum} is EVEN PARITY")
elif x%2!=0:
    y=list(strnum)
    print(f"BEFORE APPENDING :...\t{y}")
    print("..................................")
    y.append("1")
    z=y.count("1")
    print(f"no of 1,s are {z}.")
    print(f"After APPENDING:....\t{y}")
else:
    pass
    



