def merge_array(arr, strIdx,mid,lastIdx):
    merged=[]
    j=mid+1
    i=strIdx
    while i<=mid and j<=lastIdx:
        if arr[i]<=arr[j]:
            
            merged.append(arr[i])
            i+=1
        else:
            
            merged.append(arr[j])
            j+=1
    
    while i<=mid:
        
        merged.append(arr[i])
        i+=1
        
    while j<=lastIdx:
        
        merged.append(arr[j])
        j+=1
        
    arr[strIdx:lastIdx+1] = merged    
    
          
   # for i in range(len(merged)):


def merge_sort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge_array(arr, start, mid, end)


    
        


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if  __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    merge_sort(arr,0,len(arr)-1)
    
    print("Sorted array: ", end="")
    print_array(arr)