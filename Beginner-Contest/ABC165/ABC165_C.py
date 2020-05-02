N,M,Q=map(int, input().split())
abcd=list()
cnt=0
for i in range(Q):
    abcd.append(tuple(map(int, input().split())))

for i in range(N):
    A=list()
    for j in range(M+1-N, M+1):
        A.append(j)
    print(A)
    if A[abcd[i][1]-1]-A[abcd[i][0]]>=abcd[i][2]:
            cnt=max(cnt, abcd[i][3])

print(cnt)