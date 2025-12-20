def sumPair(arr, k):
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
    
    for i in range(n):
        
        if  (arr[left]+arr[right])==k:
            return True
            
        elif (arr[left]+arr[right])>k:
            right-=1
        else:
            left+=1
            
        
        

if __name__ == "__main__":
    #arr = [4, 3, 8, 6, 11, 17, 14]
    arr = [-3, -1, 0, 1, 2]
    target = -2
    sumExist=sumPair(arr,target)
    print(sumExist)