N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

if N >= M:
    print(0)
else:
    sub = [0]*(M-1)
    for i in range(M-1):
        sub[i] = X[i+1]-X[i]
    sub.sort()

    ans = 0
    for i in range(M-N):
        ans += sub[i]
    print(ans)
