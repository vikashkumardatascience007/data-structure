def countEvenOdd(arr):
    evenCount=0
    oddCount=0
    
    for i in range(len(arr)):
        if arr[i] % 2 ==0:
            evenCount+=1
        else:
            oddCount+=1
            
    print(f'odd count is:-{oddCount}')
    print(f'even count is:-{evenCount}')


if __name__ == "__main__":
    arr = [4, 3, 8, 6, 11, 17, 14]

    countEvenOdd(arr)
