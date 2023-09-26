'''
a=2   
b=3
hcf=1
lcm=6
       a*b
HCF=  _____________

         lcm

         
         a*b=lcm*hcf
'''    
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
for i in range(1,(a*b)+1):
    if i%a==0 and i%b==0:
        print("LCM is",i)
        LCM=i
        break
HCF=int((a*b)/LCM)
print(f"HCF of {a} and {b} is {HCF}")