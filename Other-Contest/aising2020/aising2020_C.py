from collections import Counter
n = int(input())
l = list()
for i in range(1,101):
    l.append((i, i**2))
# print(l)
c = Counter()
for X in l:
    for Y in l:
        for Z in l:
            x = X[0]
            y = Y[0]
            z = Z[0]
            c[X[1]+Y[1]+Z[1]+x*y+y*z+x*z] += 1

for i in range(1, n+1):
    print(c[i])
