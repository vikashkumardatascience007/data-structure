def freqCount(st):
    res={}
    for ch in st:
        if ch in res:
            res[ch]=res[ch]+1
        else:
            res[ch]=1
            
    print(res)
        
    
    





if __name__ == "__main__":
    st='elephantaatthtpllllp' 

    freqCount(st)