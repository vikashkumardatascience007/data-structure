def frequencyItem(arr):
    temp={}
    for i in range(len(arr)):
        if arr[i] in temp.keys():
            temp[arr[i]]=temp[arr[i]]+1
        else:
            temp[arr[i]]=1
            
    print(temp)


if __name__ == "__main__":
    arr = [1,9, 2, 3, 9, 4, 2, 5, 5, 9, 3, 3, 2]
    frequencyItem(arr)