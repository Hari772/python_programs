''' if global and local varible has same name  then first preference goes to local variable'''
a=20# global variable
def display():
    a=30#local variable//first preference goes to local variable
    print(a)#if local and global variable are same
    
display()
print(a)
