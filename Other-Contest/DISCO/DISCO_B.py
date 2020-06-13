N=int(input())
A=list(map(int, input().split()))
S=M=sum(A)
cnt=0
for a in A:
    cnt+=a
    M=min(M, abs(S-2*cnt))
print(M)