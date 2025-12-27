def checkAnagram(s1,s2):
    isAna=False
    if len(s1) !=len(s2):
        return isAna
    
    has={}
    for i in s1:
        if i in has.keys():
            has[i]=has[i]+1
        else:
            has[i]=1
            
    for i in s2:
        if(i not in has or has[i] ==0):
            isAna=False
        else:
            isAna=True

        has[i]-=1  
    return isAna
    

if __name__=='__main__':
    
    s1 = "eret"
    s2 = "tree"
    has= checkAnagram(s1,s2)
    print(has)
    