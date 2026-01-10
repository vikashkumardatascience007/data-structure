arr=[3,8,11,9,2,5]

def lar_small_num(arr):
# getting largest & smallest1 number
    k=0 
    largeVal=0
    smallVal=arr[0]
    for i in range(0,len(arr)):
        # largest val in array
        if largeVal<arr[i]:
            largeVal=arr[i]
        
        # samllest val in array
        if smallVal>arr[i]:
            smallVal=arr[i]
        
    print(f'laregst value in given array : -> {largeVal}')
    print(f'smallest value in given array : -> {smallVal}')
    
    

lar_small_num(arr)
            
        