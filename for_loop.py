''' 
Python For Loops
1.A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

2.This is less like the for keyword in other programming languages, and works more like an 
iterator method as found in other object-orientated programming languages.

3.With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''
'''x=["A","B","C"]
for i in x:
    print(i)'''
# looping through  a string
# x="python"
# print(x)
# for i in "java":
#     print(i)
""" how to use range function 

range(start(0),end(by default increment  by 1),step)

"""

#printing 10 numbers
'''for i in range(0,11,3):
    if i==0:
        pass
    else:
        print(i)'''
# printing odd and even number in python
for i in range(21):
    if i==0:
        pass
    elif i%2==0:
        print("even numbers")
        print(i)
    else:
        print("odd numbers")
        print(i)