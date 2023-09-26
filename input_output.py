'''a=input()# single charcter
b=input()# sting
c=int(input())#integer
d=float(input())#float->decimal number

print(a)
print(b)
print(c)
print(d)
x,y=5,6
print(x,y)
a=int(input())
b=int(input())
print(a,end=" and ")#print(a,end=" ")->by default next line will be printed
print(b)
a,b=input().split()#taking input at a time as a string
print(type(a))
print(type(b))
print(a)
print(b)
print(int(a))
print(int(b))
print(type(int(a)))
x,y=map(int,input().split())# taking input as  a integer at  a time
print(x)
print(y)
print(type(x))'''
x,y=map(int,input("Enter the numbers:").split(","))#very important
print(x)
print(y)

