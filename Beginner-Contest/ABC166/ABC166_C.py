N, M = map(int, input().split())
H = list(map(int, input().split()))
r = list()
for _ in range(N):
    r.append([])
for i in range(M):
    A, B = map(int, input().split())
    A-=1
    B-=1
    r[A].append(H[B])
    r[B].append(H[A])

cnt = 0
i = 0
for l in r:
    if len(l) == 0:
        cnt += 1
    elif max(l) < H[i]:
        cnt += 1
    i += 1

print(cnt)
