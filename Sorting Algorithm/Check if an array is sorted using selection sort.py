# Python program for implementation of Selection Sort

def selection_sort(arr):
    if len(arr)==0:
        return
    
    minIdx=0
    for i in range(0,len(arr)-1):
        #minIdx=arr[i]
        for j in range(i+1, len(arr)):
            if arr[minIdx]>arr[j]:
                minIdx=j
        
        arr[i],arr[minIdx]=arr[minIdx],arr[i]
 
        
def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()
        
        
if  __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr)