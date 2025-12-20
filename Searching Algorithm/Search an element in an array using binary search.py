def binarySearch(arr,k):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
        
    left=0
    right=n-1
    print(arr)
    
    for i in range(n):
        if arr[left]==k or arr[right]==k:
            return True
            
        elif arr[left]<k:
            left+=1
        elif arr[right]>k:
            right-=1

if __name__ == "__main__":
    arr = [4, 3, 8, 6, 11, 17, 14]
    isEleExist= binarySearch(arr,6)
    print(isEleExist)
   