def twoSum(arr, k):
    
    i=0
    j=len(arr)-1
    arr.sort()
    
    while i<j:
        
        if arr[i]+arr[j]==k:
            return True
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
    return False

        













if __name__ == "__main__":
    #arr = [4, 3, 8, 6, 11, 17, 14]
    arr = [0, -1, 2, -3, 1]
    target = -2
    isTwoSumExists=twoSum(arr,target)
    print(isTwoSumExists)