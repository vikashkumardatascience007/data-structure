def reverseStr(st):
    return st[::-1]

#Another approach
def revStr(st):
    s=''
    for i in range(len(st)-1,-1,-1):
        s=s+st[i]
    return s

if __name__ == "__main__":
    st='kumar' 

    x=revStr(st)
    print(x)
