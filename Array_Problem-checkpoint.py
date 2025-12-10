# Given an array, we have to find the largest element in the array.
# Brute force approach
arr = [2,5,1,3,0,7,4]

res=0
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]= arr[j]
            arr[j]=temp



res=arr[-1:]
arr[-1]




