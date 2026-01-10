arr=[3,8,11,9,2,5]

def reverseArr(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i])
    
reverseArr(arr)

# or


def revserArr_1(arr):
    print(arr[::-1])
    
revserArr_1(arr)



## Two different approaches discussed