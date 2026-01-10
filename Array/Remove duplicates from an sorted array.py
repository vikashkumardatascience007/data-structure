def removeDuplicates(arr):
    i=0
    j=1
    while j < len(arr):
        if arr[i]==arr[j]:
            j+=1
        else:
            i+=1
            arr[i], arr[j]=arr[j],arr[i]
            j+=1
    print(arr[:i+1])







if __name__ == "__main__":
    arr = [1, 1, 2, 3, 4, 4, 4, 5]
    removeDuplicates(arr)