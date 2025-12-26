
def maxSum(arr,k):
    i=0
    n=len(arr)
    win_sum=sum(arr[:k])
    tempSum=0
    
    for i in range(n-k):
        tempSum=tempSum-arr[i]+arr[k+i]
        if tempSum>win_sum:
            win_sum=tempSum
    return win_sum
            


if __name__ == "__main__":
    #arr = [4, 3, 8, 6, 11, 17, 14]
    arr = [5, 2, -1, 0, 3]
    k = 3
    x=maxSum(arr,k)
    print(x)
    6-2+3