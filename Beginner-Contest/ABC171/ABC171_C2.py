n = int(input())
alp = list()
for ch in '-abcdefghijklmnopqrstuvwxyz':
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
l = Base_10_to_n(n, 26)
#print(l)
for i in l:
    if alp[i]!='-':
        s = alp[i] + s
    elif x==len(l)-1:
        s = 'a' + s 
    x+=1 

print(s)
