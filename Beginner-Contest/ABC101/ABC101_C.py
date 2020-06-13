N, K = map(int, input().split())
A = list(map(int, input().split()))
eq = 1
cnt = int()
while eq<N:
    eq += (K-1)
    #print(cnt, eq)
    cnt +=1

print(cnt)