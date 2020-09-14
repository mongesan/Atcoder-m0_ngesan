n = int(input())
S = str(input())
r = []
g = []
b = []
for i in range(n):
    if S[i] == 'R':
        r.append(i)
    elif S[i] == 'G':
        g.append(i)
    else:
        b.append(i)
#print(r, g, b)
ans = 0
for R in r:
    for G in g:
        i = min(R, G)
        j = max(R, G)
        for B in b:
            if j < B:
                if j-i != B-j:
                    ans += 1
            elif B < i:
                if j-i != i-B:
                    ans += 1
            else:
                if j-B != B-i:
                    ans += 1

print(ans)
