def checkVowelNAndConst(st):
    i=0
    j=0
    
    for ch in st:
        if ch == 'a' or ch == 'e' or  ch == 'i' or ch == 'o' or ch == 'u':
            i+=1
        else:
            j+=1
            
    
    print(f'No of vowel is: {i}')
    print(f'No of conspnants is: {j}')
            
            


if __name__ == "__main__":
    st='aoo Bowd  adcu exam' 

    checkVowelNAndConst(st)
 