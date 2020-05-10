N, K = map(int, input().split())
A = list(map(int, input().split()))
Kr = [False]*N
r = [0]
p = 0
cnt = 1
while True:
    Kr[p]=True
    #無限ループチェッカー
    if Kr[A[p]-1] == 1:
        sp = r.index(A[p])
    cnt+=1