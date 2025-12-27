def subArrayWithoutRepeat(st):
    max_len=0
    cur_len=0
    ls=[]
    for i in range(0,len(st)):
        if st[i] in ls:      
            cur_len=len(ls)
            ls=[]
            ls.append(st[i])
        else:
            ls.append(st[i])
            
        if cur_len>max_len:
            max_len=cur_len
        
    return max_len
        
            
           

if __name__ == "__main__":
    s = "abcabcbb"
    
    s1 = "bbbbb"
    
    s2 = "pwwkew"
    x=subArrayWithoutRepeat(s)
    print(x)