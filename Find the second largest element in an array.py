arr=[3,8,11,9,2,5]


def secLargest(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted:", arr)
    print("Second Largest:", arr[-2])
    
    
secLargest(arr)

    
    