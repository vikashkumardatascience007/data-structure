def anagramList(arr):
    re = {}
    c=0
    for w in arr:
        s = ''.join(sorted(w))

        if s not in re:
            re[s] = []

        re[s].append(w)
    
    res=[]
    for v in re.values():
        res.append(v)

    print(res)


if __name__ == "__main__":
    w = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagramList(w)
