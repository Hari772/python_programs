list1=[]
num=int(input("Enter the value of num"))
print("list values:\n")
for k in range(num):
    list1.append(int(input()))
print("Unsorted list:",list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]= list1[i+1],list1[i]
print("sorted list:",list1)
