n = int(input())
A = list(map(int, input().split()))
m = 1000
for i in range(n-1):
    t = m//A[i]
    if A[i] < A[i+1]:
        m -= t*A[i]
        m += t*A[i+1]
print(m)
