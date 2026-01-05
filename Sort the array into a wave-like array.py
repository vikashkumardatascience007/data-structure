def waveArray(arr):

    for i in range(1,len(arr),2):
        if  arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    print(f'then wav array is :- {arr}')

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    waveArray(arr)
