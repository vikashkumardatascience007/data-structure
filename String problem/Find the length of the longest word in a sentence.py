def longWord(st):
    length=0
    res=''
    st=st.split(' ')
    for word in st:
        temp=len(word)
        if temp>length:
            res=word
            length=temp
    
    print(f'{res} is word of longest length is {length}')
            


if __name__ == "__main__":
    st='My name is Vikash and my engineering degree is COmputer Science' 

    longWord(st)