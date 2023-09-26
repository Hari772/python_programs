def binary_search(arr,key):
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    found=False
    while low<=high and not found:
        if key==arr[mid]:
            found=True
        elif key>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("print key is found")
    else:
        print("key is not found")
        

arr=[9,8,6,5,4,3,7,2,1,10,0]
arr.sort()
print(arr)
key=int(input("Enter the key\n"))
binary_search(arr,key)
