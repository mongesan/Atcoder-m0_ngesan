for i2 in range(1,704):
    alp=['z']
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
    l = Base_10_to_n(i2, 26)
    l.reverse()
    #print(l)
    print(l)
    for i in l:
        s += alp[i]
    print(i2,s)
