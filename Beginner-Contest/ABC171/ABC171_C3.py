for i2 in range(1,100):
    alp = list()
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        alp.append(ch)
    def Base_10_to_n(X, n):
        X_dumy = X
        out = []
        while X_dumy > 0:
            out.append(X_dumy % n)
            X_dumy = int(X_dumy/n)
        return out


    x = int()
    s = str()
    l = Base_10_to_n(i2, 27)
    #print(l)
    print(l)
    for i in l:
        if x == len(l)-1:
            alp.insert(0, '-')
        s = alp[i] + s
        x += 1

    print(i2,s)
