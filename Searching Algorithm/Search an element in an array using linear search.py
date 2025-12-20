def searchEle(arr, k):
    isExists:bool=False
    for i in range(len(arr)):
        if k==arr[i]:
            isExists=True

    if isExists:
        print(f'{k} exists')
    else:
        print(f' {k} not exists')


if __name__ == "__main__":
    arr = [4, 3, 8, 6, 11, 17, 14]

    searchEle(arr,36)