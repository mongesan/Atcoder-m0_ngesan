from collections import Counter
N, K = map(int, input().split())
l = [0]*N
for i in range(K):
    d = int(input())
    tmp = list(map(int, input().split()))
    for j in tmp:
        l[j-1] += 1

c = Counter(l)
print(c[0])
