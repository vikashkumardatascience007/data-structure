def revWordInSent(st):
    st=st.split(' ')
    sent=''
    for word in range(len(st)-1,-1,-1):
        sent=sent+' '+st[word]
    print(sent)


if __name__ == "__main__":
    st='My name is vikash kumar' 

    x=revWordInSent(st)