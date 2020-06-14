n=int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
m=-1

for i in range(n):
    m=max(m, sum(A1[:i+1])+sum(A2[i:]))

print(m)