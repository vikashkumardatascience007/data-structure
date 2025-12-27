def checkAnagram(s1,s2):
    isAna=False
    if len(s1) !=len(s2):
        return isAna
    
    has=set()
    for i in s1:
        has.add(i)
            
    for i in s2:
        if(i in has):
            isAna=True
        else:
            isAna=False
            
    return isAna
    

if __name__=='__main__':
    
    s1 = "allergy"
    s2 = "gyallrey"
    has= checkAnagram(s1,s2)
    print(has)
    