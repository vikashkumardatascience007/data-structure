def getSum(arr):
    tot=0
    maxSum=0
    for i in range(0, len(arr)):
        tot+=arr[i]
        maxSum=max(maxSum,tot)
        
        if tot<0:
            tot=0
    
    return maxSum

if __name__=='__main__':
    
    arr=[3,-4,0]
    print(f'max sum of sub array:- {getSum(arr)}')