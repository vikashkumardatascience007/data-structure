def removeDup(st):
    res=''
    for ch in st:
        if ch not in res:
            res=res+ch
            
    print(res)


if __name__ == "__main__":
    st='HappyNewYear' 

    removeDup(st)