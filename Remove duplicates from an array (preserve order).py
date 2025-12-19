
def removeDuplicates(arr):
    tempArr=[]
    for i in range(0,len(arr)):
        #tempArr.append(arr[i])
        if arr[i] not in tempArr:
            tempArr.append(arr[i])
        
    print(tempArr)
    


if __name__ == "__main__":
    arr = [1,9, 2, 3, 9, 4, 2, 5, 5]
    removeDuplicates(arr)