N, K = map(int, input().split())
A = list(map(int, input().split()))
Kn = [0]*N
l = [A[0]]
p = A[1]
i = 1
while True:
    Kn[p] = 1
    print(p)
    if Kn[A[p]-1] == 1:
        print(l)
        sp = l.index(A[p]-1)
        ep = len(l)-1
        break
    elif i == K:
        print(p+1)
    l.append(A[p])
    p = A[p]-1
    i += 1
l = l[sp:]
K -= sp
print(l, K)
#print(sp, ep, l, K)
if K % len(l) == 0:
    print(l[len(l)-1])
else:
    print(l[K % (len(l)-1)])
