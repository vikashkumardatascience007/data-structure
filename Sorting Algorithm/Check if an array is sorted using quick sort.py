def partition(arr, st, en):
    piv=arr[en]
    j=st
    idx=st-1
    
    for i in range(st,en):
        if arr[i]<=piv:
            idx+=1
            arr[i], arr[idx]=arr[idx],arr[i]
    idx+=1
    arr[idx], arr[en]=arr[en],arr[idx]  
    
    return idx
        
        
    

def quick_sort(arr,st, en):
    if st<en:
        pivIdx=partition(arr,st,en)
        
        quick_sort(arr,st, pivIdx-1)
        quick_sort(arr,pivIdx+1,en)
    
    



def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if  __name__ == "__main__":
    arr = [64, 25, 12, 90, 11,80]
    
    print("Original array: ", end="")
    print_array(arr)
    
    quick_sort(arr,0,len(arr)-1)
    
    print("Sorted array: ", end="")
    print_array(arr)