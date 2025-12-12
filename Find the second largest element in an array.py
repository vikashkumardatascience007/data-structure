arr=[3,8,11,9,2,5]


def secLargest(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1], arr[i]
        #else:
            #arr[i+1],arr[i]=arr[i], arr[i+1]
            
        
    print(arr)
    
    
secLargest(arr)
    
    