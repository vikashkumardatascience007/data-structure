def removeElement(arr, ele):
    k = 0
    t=[]
    for i in range(len(arr)):
        if arr[i] != ele:
            arr[k] = arr[i]  

            k += 1 
            t.append(arr[k])
    print(t,'eeeeee')            
              
    return k 
  
if __name__ == "__main__":
    arr = [0, 1, 3, 0, 2, 2, 4, 2]
    ele = 2
    print(removeElement(arr, ele))