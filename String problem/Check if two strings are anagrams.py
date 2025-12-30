def checkAnagram(s1,s2):
    res={}
    isTrue=False
    
    for ch in s1:
        if ch in res:
            res[ch]=res[ch]+1
        else:
            res[ch]=1
    
    for ch in s2:
        if ch in res:
             res[ch]=res[ch]-1
             isTrue=True
             print(res)
        else:
             isTrue=False
            
            
    print(f'given string is anagram is : - {isTrue}')
        



if __name__ == "__main__":
    s1 = "allergy" 
    s2 = "llaergyy"

    checkAnagram(s1,s2)