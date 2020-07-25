n,k=map(int, input().split())
A=list(map(int, input().split()))
for i in range(n-k):
    if A[i]<A[i+k]:
        print('Yes')
    else:
        print('No')